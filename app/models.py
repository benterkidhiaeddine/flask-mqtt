from . import db
from datetime import datetime
 #this is used to simplify the jsonification of objects queried by the database
class Serializer(object):
    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
 # Define a model for the aggregated data
class AggregatedData(db.Model,Serializer):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(255))
    value = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    def serialize(self):
        return {
            "topic" : self.topic,
            "value" : self.value,
        }