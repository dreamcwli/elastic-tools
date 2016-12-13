# Elastic Tools

## Requirements

* Docker and Docker Compose: run Elasticsearch and Kibana using Docker
* Python 2.7 and PyMongo: import data from MongoDB binary export

## Usage

Run Elasticsearch and Kibana using Docker:
```shell
docker-compose -f docker/docker-compose.yml up -d
```

Import data from MongoDB binary export:
```shell
python scripts/mongodb-import.py export.bson
```
