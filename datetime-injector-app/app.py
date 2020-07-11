"""DateTime injector Web Application

This flask application allows messages to be sent and read to a kafka broker

The api listens on TCP port 5000 for either GET or POST requests that provide the
respective communication to the kafka broker.

This file contains the following functions:

    * index - A simple welcome message to verify the API is listening on port 5000
    * insert_message - uses a kafka producer to send serialised string messages
    * basic_consume_loop - polls the 'datetime-topic' for any new messages/records
    * not_found - sends a json formatted message to requester when error 404 is returned
"""

#!flask/bin/python
from flask import Flask, jsonify, abort, make_response
from datetime import datetime
from confluent_kafka import Producer, Consumer
import socket
import json

app = Flask(__name__)

# configuration used for the kafka producer
producer_conf = {
    # 'bootstrap.servers': 'localhost:9092',
    'bootstrap.servers': 'my-confluent-cp-kafka:9092',
    'client.id': socket.gethostname()
}
p = Producer(producer_conf)

# configuration used for the kafka consumer
consumer_conf = {
    # 'bootstrap.servers': 'localhost:9092',
    'bootstrap.servers': "my-confluent-cp-kafka:9092",
    'group.id': 'mygroup',
    'client.id': socket.gethostname(),
    'enable.auto.commit': True,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'earliest'}
}
c = Consumer(consumer_conf)


@app.route('/')
def index():
    return jsonify({'Message': 'Welcome to my datetime generator application'}), 200

# TODO allow my api to accept messages
@app.route('/producer/insert', methods=['POST'])
def insert_message():
    key = 'time'
    dateTimeObj = str(datetime.now())
    # TODO: de-serialise to json on comsumer end
    p.produce('datetime-topic', key=key, value=dateTimeObj)
    response = {
        'Status': 'Message Produced',
        'Message': {'Key': key, "Value": dateTimeObj}
    }
    return jsonify(response)


@app.route('/consumer/printlog', methods=['GET'])
def basic_consume_loop():
    c.subscribe(['datetime-topic'])

    try:
        while True:
            msg = c.poll(0.1)
            if msg is None:
                # No message available within timeout.
                # Initial message consumption may take up to
                # `session.timeout.ms` for the consumer group to
                # rebalance and start consuming
                continue
            elif not msg.error():
                return ('Received message: {0}'.format(msg.value()))
            else:
                return ('error: {}'.format(msg.error()))
    finally:
        # TODO: list out messages consumed
        c.commit()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
