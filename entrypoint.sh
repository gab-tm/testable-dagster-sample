#!/bin/sh
docker-compose -f docker-compose-dev.yaml down -v
docker-compose -f docker-compose-dev.yaml build --no-cache
docker-compose -f docker-compose-dev.yaml up -d