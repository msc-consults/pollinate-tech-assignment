#!flask/bin/python
from flask import Flask, jsonify, abort, make_response
from datetime import datetime
from confluent_kafka import Producer

app = Flask(__name__)
p = Producer({'bootstrap.servers': 'localhost:9092'})


@app.route('/')
def index():
    return jsonify({'Message': 'Welcome to my datetime generator application'}), 200


@app.route('/producer/flush', methods=['GET'])
def flush_command():
    p.flush(30)
    return 'All messages have been produced'

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


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
