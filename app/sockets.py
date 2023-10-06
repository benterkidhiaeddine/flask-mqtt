import json
from . import app
from . import mqtt,socketio,db
from .models import AggregatedData
#subscripe to all topics
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('#')


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
    with app.app_context():
        #ignore first welcoming statment
        if message.payload.decode() == '{"1":"Hello world","2":"Welcome to the test connection"}':
            return
        #ignore data values that don't stray too much from last ones
        
        db.session.add(AggregatedData(topic = message.topic, value = message.payload.decode()))
        db.session.commit()
    socketio.emit('mqtt_message', data=data)
    


@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    print(level, buf)