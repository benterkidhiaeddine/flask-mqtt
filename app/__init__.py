import eventlet
import json
from flask import Flask 
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from settings import Config
eventlet.monkey_patch()

app = Flask(__name__)


app.config.from_object(Config)

#install flask extentions
CORS(app)
mqtt = Mqtt(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
socketio = SocketIO(app, cors_allowed_origins="*")
jwt = JWTManager(app)



from . import views, models, sockets

