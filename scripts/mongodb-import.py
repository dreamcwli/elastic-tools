import bson
import json

from argparse import ArgumentParser
from bson import json_util
from urllib2 import Request, urlopen

parser = ArgumentParser(description='Import data from MongoDB binary export.')
parser.add_argument('filename', help='filename of MongoDB binary export')
args = parser.parse_args()

binary = open(args.filename, 'rb').read()
data = bson.decode_all(binary)
count = 1
bulk = ''
for datum in data:
    action = json.dumps(
        {
            'index': {
                '_index': 'search',
                '_type': 'tag',
                '_id': str(count)
            }
        }
    )
    bulk += action + '\n'
    del datum['_id']
    source = json.dumps(datum, default=json_util.default)
    bulk += source + '\n'
    count += 1

headers = {
    'Content-Type': 'application/octet-stream'
}
request = Request(url='http://localhost:9200/_bulk', data=bulk, headers=headers)
response = urlopen(request).read()
data = json.loads(response)
count = 0
for item in data['items']:
    if 'error' in item['index']:
        error = json.dumps(item['index']['error'], indent=2)
        print(error)
    else:
        count += 1
print('imported %d items' % count)
