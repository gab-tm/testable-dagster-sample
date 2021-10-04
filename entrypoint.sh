#!/bin/sh
docker-compose -f docker-compose-dev.yaml up -d --build cloudsql_proxy
docker-compose -f docker-compose-dev.yaml up -d --build pipelines
docker-compose -f docker-compose-dev.yaml up -d --build dagit daemon