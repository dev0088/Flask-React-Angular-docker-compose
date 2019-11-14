#!/bin/sh

# Stop previous dockers
docker-compose stop
docker-compose down

# Run dockers as daemon
docker-compose up -d --build

# Remove caches
# yes | docker container prune
# yes | docker network prune
# yes | docker image prune


