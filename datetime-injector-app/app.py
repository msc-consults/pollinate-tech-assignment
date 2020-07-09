#!flask/bin/python
from flask import Flask, jsonify, make_response
from confluent_kafka import Producer

app = Flask(__name__)
p = Producer({'bootstrap.servers': 'localhost:9092'})
id = 1

@app.route('/')
def index():
    global id
    id += 1
    key = 'hello-' + str(id)
    message = 'world'

    # TODO: serialise this to json, or de-serialise to json on comsumer end
    p.produce('mytopic', key=key, value=message)
    return jsonify({'Status': 'Message Produced', 'Key': key, "Value": message}), 201


@app.route('/producer/flush', methods=['GET'])
def flush_command():
    p.flush(30)
    return 'All messages have been produced'

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
