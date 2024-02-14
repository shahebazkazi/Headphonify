#!/usr/bin/bash

# Define the main Node.js image name
MAIN_NODEJS_IMAGE="node:16 "

# Remove all Docker images except the main Node.js image
docker images -q | grep -v $MAIN_NODEJS_IMAGE | xargs -I {} docker rmi -f {}
