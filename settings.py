import os

# name of the directory where the project resides
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = (
        os.environ.get("SECRET_KEY") or "random-password-that-you-will-never-guess"
    )
    # define where the database is going to reside it gets from the environment variable if it exist else it will give a default value
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL") or f"sqlite:///{os.path.join(basedir,'app.db')}"
    )

    MQTT_BROKER_URL = '13.38.173.241'
    MQTT_BROKER_PORT = 1883
    MQTT_USERNAME = ''
    MQTT_PASSWORD = ''
    MQTT_KEEPALIVE = 5
    MQTT_TLS_ENABLED = False

    TEMPLATES_AUTO_RELOAD = True
