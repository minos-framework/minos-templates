#!/bin/sh

set -e

ROOT_DIR=$(dirname "$0")
BUILD_DIR=$(dirname "$0")/.build

mkdir -p "$BUILD_DIR"

echo "Building Microservice Init Template..."
tar -czf "$BUILD_DIR/microservice-init.tar.gz" -C "$ROOT_DIR/microservice/init" .

echo "Building Microservice Python Init Template..."
tar -czf "$BUILD_DIR/microservice-python-init.tar.gz" -C "$ROOT_DIR/microservice/language/python/init" .

echo "Building Microservice Python Package Manager Poetry Template..."
tar -czf "$BUILD_DIR/microservice-python-package-manager-poetry.tar.gz" -C "$ROOT_DIR/microservice/language/python/package-manager/poetry" .

echo "Building Microservice Python Package Manager Pip Template..."
tar -czf "$BUILD_DIR/microservice-python-package-manager-pip.tar.gz" -C "$ROOT_DIR/microservice/language/python/package-manager/pip" .

echo "Building Microservice Python Deploy Docker Template..."
tar -czf "$BUILD_DIR/microservice-python-deploy-docker.tar.gz" -C "$ROOT_DIR/microservice/language/python/deploy/docker" .

echo "Building Microservice Python Deploy Kubernetes Template..."
tar -czf "$BUILD_DIR/microservice-python-deploy-kubernetes.tar.gz" -C "$ROOT_DIR/microservice/language/python/deploy/kubernetes" .

echo "Building Project Init Template..."
tar -czf "$BUILD_DIR/project-init.tar.gz" -C "$ROOT_DIR/project/init" .

echo "Building Project API Gateway Minos Init Template..."
tar -czf "$BUILD_DIR/project-apigateway-minos-init.tar.gz" -C "$ROOT_DIR/project/apigateway/minos/init" .

echo "Building Project API Gateway Minos Deploy Docker Compose Template..."
tar -czf "$BUILD_DIR/project-apigateway-minos-deploy-docker-compose.tar.gz" -C "$ROOT_DIR/project/apigateway/minos/deploy/docker-compose" .

echo "Building Project API Gateway Minos Deploy Kubernetes Template..."
tar -czf "$BUILD_DIR/project-apigateway-minos-deploy-kubernetes.tar.gz" -C "$ROOT_DIR/project/apigateway/minos/deploy/kubernetes" .

echo "Building Project API Gateway Minos Deploy Remote Template..."
tar -czf "$BUILD_DIR/project-apigateway-minos-deploy-remote.tar.gz" -C "$ROOT_DIR/project/apigateway/minos/deploy/remote" .

echo "Building Project Broker Kafka Init Template..."
tar -czf "$BUILD_DIR/project-broker-kafka-init.tar.gz" -C "$ROOT_DIR/project/broker/kafka/init" .

echo "Building Project Broker Kafka Deploy Docker Compose Template..."
tar -czf "$BUILD_DIR/project-broker-kafka-deploy-docker-compose.tar.gz" -C "$ROOT_DIR/project/broker/kafka/deploy/docker-compose" .

echo "Building Project Broker Kafka Deploy Kubernetes Template..."
tar -czf "$BUILD_DIR/project-broker-kafka-deploy-kubernetes.tar.gz" -C "$ROOT_DIR/project/broker/kafka/deploy/kubernetes" .

echo "Building Project Broker Kafka Deploy Remote Template..."
tar -czf "$BUILD_DIR/project-broker-kafka-deploy-remote.tar.gz" -C "$ROOT_DIR/project/broker/kafka/deploy/remote" .

echo "Building Project Database Postgres Init Template..."
tar -czf "$BUILD_DIR/project-database-postgres-init.tar.gz" -C "$ROOT_DIR/project/database/postgres/init" .

echo "Building Project Database Postgres Deploy Docker Compose Template..."
tar -czf "$BUILD_DIR/project-database-postgres-deploy-docker-compose.tar.gz" -C "$ROOT_DIR/project/database/postgres/deploy/docker-compose" .

echo "Building Project Database Postgres Deploy Kubernetes Template..."
tar -czf "$BUILD_DIR/project-database-postgres-deploy-kubernetes.tar.gz" -C "$ROOT_DIR/project/database/postgres/deploy/kubernetes" .

echo "Building Project Database Postgres Deploy Remote Template..."
tar -czf "$BUILD_DIR/project-database-postgres-deploy-remote.tar.gz" -C "$ROOT_DIR/project/database/postgres/deploy/remote" .

echo "Building Project Database Redis Init Template..."
tar -czf "$BUILD_DIR/project-database-redis-init.tar.gz" -C "$ROOT_DIR/project/database/redis/init" .

echo "Building Project Database Redis Deploy Docker Compose Template..."
tar -czf "$BUILD_DIR/project-database-redis-deploy-docker-compose.tar.gz" -C "$ROOT_DIR/project/database/redis/deploy/docker-compose" .

echo "Building Project Database Redis Deploy Kubernetes Template..."
tar -czf "$BUILD_DIR/project-database-redis-deploy-kubernetes.tar.gz" -C "$ROOT_DIR/project/database/redis/deploy/kubernetes" .

echo "Building Project Database Redis Deploy Remote Template..."
tar -czf "$BUILD_DIR/project-database-redis-deploy-remote.tar.gz" -C "$ROOT_DIR/project/database/redis/deploy/remote" .

echo "Building Project Deploy Docker Compose Template..."
tar -czf "$BUILD_DIR/project-deploy-docker-compose.tar.gz" -C "$ROOT_DIR/project/deploy/docker-compose" .

echo "Building Project Discovery Minos Init Template..."
tar -czf "$BUILD_DIR/project-discovery-minos-init.tar.gz" -C "$ROOT_DIR/project/discovery/minos/init" .
  
echo "Building Project Discovery Minos Deploy Docker Compose Template..."
tar -czf "$BUILD_DIR/project-discovery-minos-deploy-docker-compose.tar.gz" -C "$ROOT_DIR/project/discovery/minos/deploy/docker-compose" .

echo "Building Project Discovery Minos Deploy Kubernetes Template..."
tar -czf "$BUILD_DIR/project-discovery-minos-deploy-kubernetes.tar.gz" -C "$ROOT_DIR/project/discovery/minos/deploy/kubernetes" .

echo "Building Project Discovery Minos Deploy Remote Template..."
tar -czf "$BUILD_DIR/project-discovery-minos-deploy-remote.tar.gz" -C "$ROOT_DIR/project/discovery/minos/deploy/remote" .

echo "Building Project Deploy Docker Compose Template..."
tar -czf "$BUILD_DIR/project-deploy-docker-compose.tar.gz" -C "$ROOT_DIR/project/deploy/docker-compose" .

echo "Building Project Deploy Kubernetes Template..."
tar -czf "$BUILD_DIR/project-deploy-kubernetes.tar.gz" -C "$ROOT_DIR/project/deploy/kubernetes" .