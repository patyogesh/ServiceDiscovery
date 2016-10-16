#!/bin/bash

# Remove the Service Discovery containers and images.
                                                                                                                                                                                                          
# Variables. Kind of hardcoded based on names in properties file for kafka.
sd="bhavneshgugnani"
latest="latest"
zk="zookeeper"
broker="broker"
producer="producer"
consumer="consumer"

# Stop and Remove local container/images for avoiding clash
echo "CLEANING UP OLD IMAGES."
docker stop ${zk}
docker stop ${broker}
docker stop ${producer}
docker stop ${consumer}

docker rm -f ${zk}
docker rm -f ${broker}
docker rm -f ${producer}
docker rm -f ${consumer}

docker rmi ${sd}/${zk}
docker rmi ${sd}/${broker}
docker rmi ${sd}/${producer}
docker rmi ${sd}/${consumer}
echo "CLEANUP COMPLETE."

