import eventlet
import json
from flask import Flask, render_template
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from settings import Config
eventlet.monkey_patch()

app = Flask(__name__)

app.config.from_object(Config)

CORS(app)
mqtt = Mqtt(app)
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('#')
@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('publish')
def handle_publish(json_str):
    data = json.loads(json_str)
    mqtt.publish(data['topic'], data['message'])


@socketio.on('subscribe')
def handle_subscribe(json_str):
    data = json.loads(json_str)
    mqtt.subscribe(data['topic'])


@socketio.on('unsubscribe_all')
def handle_unsubscribe_all():
    mqtt.unsubscribe_all()


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    socketio.emit('mqtt_message', data=data)


@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    print(level, buf)

