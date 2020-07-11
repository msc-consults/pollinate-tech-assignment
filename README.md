# pollinate-tech-assignment
Pollinate - Platform Engineering Tech Assignment - v3.0

## Introduction

This project is designed to demonstrate the use of Kafka, particularly the ability to host Kafka in a kubernetes cluster.

Kubernetes, out of the box supports the following:

- high availability
- elasticity / scalability

In addition, this project further alludes to the support for data replication and data recovery, through the means of Confluent's Kafka replicator or MirrorMaker

## What's Included in this Project

Each of the items below contain a link to a more detailed overview of that area, so please do check this out to understand more about the project.

1. [High level design document](HLD.pdf)
2. Supporting implementation
	3. [datetime-injector-app](datetime-injector-app/README.md) - the web application
	4. [Kubernetes deployment](kubernetes/README.md) of the `datetime-injector-app`
	5. [Provisioning ansible code](provision-environment/README.md), that uses Vagrant to sandbox deployment to a Ubuntu VM

## Troubles in Paradise

At the start of this project, I had envisioned that I'd be delivering a more complete solution than what I present today. 

I've broken this down into technical areas I'd hoped to made  more progress on:

### Kafka Multi-cluster Management

Setting up a kubernetes multi-node cluster where I'd be to demonstrate:

- replication of data across each of the nodes, so that if one of the nodes suffered downtime, data remained persistant
- extending the Kafka broker by offloading data from Kafka topics to a REDIS or MySQL database using Kafka Connect's 'Sink Connectors' - for an additional persistency layer
- handling a stream of incoming data and using Kafka streams and KSQL to create useful models of the data

### Ansible

Provide an all-in-one solution, summoned by issuing `vagrant up`:

- fully-functioning minikube cluster hosted on a Ubuntu VM
- Kafka brokers deployed and running on the cluster
- My web application deployed on the cluster

### Web Application

Improved set of API methods:

- Basic Auth and then Oauth on the function to produce Kafka messages
- `JSON` Serialising the messages sent to Kafka. Currently I am using the default `String` serialisation which produces unstructured messages for data ingestion

### Kubernetes

Better deployment management:

- Setting up an `NGINX` proxy and network controller to enable the `datetime-injector-app` to receive ingress traffic external to the Kubernetes cluster
- Replacing a single cluster with a production grade multi-node cluster - 1 master with 2 worker nodes (as a minimum) to demonstrate multiple datacentre scenarios 
