from flask_sqlalchemy import SQLAlchemy
from time.date import date

 # Define a model for the aggregated data
class AggregatedData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(255))
    value = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
