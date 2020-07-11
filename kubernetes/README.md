# Kubernetes Deployments

This folder holds all the Kubernetes deployments used in the local minikube cluster

### deployments/datetime-injector-app.yml

The web application has just 1 `replicaset` created, and thus, if the `pod` resource that hosts the `datetime-injector-app` container fails, another `pod` resource is provisioned.

### deployments/kafka-client.yml

Kafka client used purely for testing that the deployed Kafka broker in the K8s (Kubernetes) cluster is up and running

### Helm

There is also one Helm Chart that generates a working Kubernetes environment for the Confluent platform.

## Pre-requisites

- A single Kubernetes cluster
- Helm

## Usage

Deploy the `datetime-injector-app.yml` application to the cluster

```
# As the docker image only exists locally, 
# We must ensure it is available to the K8s cluster's local docker deamon registry
$ eval $(minikube -p minikube docker-env)

# Building the image here will register it with the K8s cluster
$ docker build -t datetime-injector-app:0.3 -f ../../datetime-injector-app/Dockerfile

# Carry-out the deployment
$ kubectl create -f deployments/datetime-injector-app.yml

```

Deploy the confluent platform, which deploys a Kafka cluster:

```
helm repo add confluentinc https://confluentinc.github.io/cp-helm-charts/
helm repo update
helm install confluentinc/cp-helm-charts --name my-confluent --version 0.5.0
```

[Return back to main README](../README.md)