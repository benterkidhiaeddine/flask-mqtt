from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


from . import app, db
from .models import AggregatedData

@app.route("/uav/<id>")
@jwt_required
def get_uav1(id):
    response = {}

    uav_data = db.session.query(AggregatedData).filter(AggregatedData.topic.startswith(f"uav{id}/")).order_by(AggregatedData.timestamp.desc()).limit(11).all()
    
    if not uav_data :
        return {"msg":"No such drone"}, 404
    for el in AggregatedData.serialize_list(uav_data):
        response[el["topic"]] = el["value"]

    return response


#Login and Auth routes
# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)   

@app.route("/fire_notification",methods = ["POST"])
def fire_notification():
    #Do some logic 
    
    #send notification to react app
    return "notification recieved"