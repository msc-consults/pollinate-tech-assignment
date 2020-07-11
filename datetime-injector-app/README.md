# Web Application - `datetime-injector-app`

This flask application allows messages to be sent and read to a kafka broker

The api listens on TCP port 5000 for either GET or POST requests that provide the respective communication to the kafka broker.

The application also supports methods to consume messages from the Kafka topic.

## Pre-requisites

- Python 3.xx
- Kafka broker + Zookeeper (either one of the following)
	- native
	- docker container
	- kubernetes deployment
- TCP port 5000 to be unoccupied

## Usage

Run the application locally:

```
$ python3 app.py

Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

Produce a new Kafka message to default Kafka topic `datetime-topic`:

```
$ curl -X POST localhost:5000/producer/insert
```

Get the current message on the Kafka topic offset:

```
$ curl localhost:5000/consumer/printlog
```

Containerise the application for deployment into Kubernetes:

```
$ docker build -t datetime-injector-app:0.3
```

[Return back to main README](../README.md)