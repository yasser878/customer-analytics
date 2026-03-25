#!/bin/bash

# create results folder on host
mkdir -p results

CONTAINER_NAME=bigdata

# check if container exists
if [ ! $(docker ps -a -q -f name=$CONTAINER_NAME) ]; then
    echo "Error: container $CONTAINER_NAME does not exist!"
    exit 1
fi

# copy files safely
docker cp $CONTAINER_NAME:/app/pipeline/data_raw.csv results/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/data_preprocessed.csv results/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/insight1.txt results/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/insight2.txt results/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/insight3.txt results/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/insight4.txt results/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/summary_plot.png results/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/clusters.txt results/ 2>/dev/null

# stop and remove the container if running
if [ $(docker ps -q -f name=$CONTAINER_NAME) ]; then
    docker stop $CONTAINER_NAME
fi

docker rm $CONTAINER_NAME 2>/dev/null

echo "All outputs copied into results folder and container removed successfully!"