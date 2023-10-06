import json
from . import app
from . import mqtt,socketio,db
from .models import AggregatedData
#subscripe to all topics
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('#')

#socket connection to add topics to the mqtt broker
@socketio.on('publish')
def handle_publish(json_str):
    data = json.loads(json_str)
    mqtt.publish(data['topic'], data['message'])

#socket to handle if a client wants to subscribe to new topics
@socketio.on('subscribe')
def handle_subscribe(json_str):
    data = json.loads(json_str)
    mqtt.subscribe(data['topic'])

#socket that handle when the client want the server to unsubscribe from all topics
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


#Define a route where the android can send a wardning to when there is fire
@app.route("/listen_to_android", methods = ["POST"])
def listen_to_android():
    socketio.emit("fire_event",{'lattitude': 90, "longitude": 80})
    return {"msg" : "message sucessful"}