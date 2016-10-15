
#!/bin/bash

# Launches the Service Discovery cluster including building images and launching them and linking them while launching

# Variables
zk="zookeeper"
broker="kafka_broker"
producer="kafka_producer"
consumer="kafka_consumer"
sd="bhavneshgugnani"
latest="latest"

echo "CLEANING UP OLD IMAGES."
# Stop and Remove local container/images for avoiding clash
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

echo "BUILDING FRESH IMAGES."
# Build fresh images
docker build -t ${sd}/${zk}:${latest} -f ./resources/ZooKeeperDockerfile ./resources
docker build -t ${sd}/${broker}:${latest} -f ./resources/KafkaDockerfile ./resources
docker build -t ${sd}/${producer}:${latest} -f ./tweet-service/producer/ProducerDockerfile ./tweet-service/producer
docker build -t ${sd}/${consumer}:${latest} -f ./tweet-service/consumer/ConsumerDockerfile ./tweet-service/consumer 
echo "IMAGES BUILD."

echo "STARTING CLUSTER COMPONENTS."
# Launch images in order and link. The names are somewhat hardcoded becuase of values in properties file for kafka
docker run -d --name ${zk} ${sd}/${zk}:${latest}
docker run -d --name ${broker} --link ${zk}:${zk} ${sd}/${broker}:${latest}
docker run -d --name ${producer} --link ${zk}:${zk} --link ${broker}:${broker} ${sd}/${producer}:${latest}
docker run -d --name ${consumer} --link ${broker}:${broker} ${sd}/${consumer}:${latest}

echo "CLUSTER SUCCESSFULLY STARTED."
