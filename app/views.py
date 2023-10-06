from . import app, db
from .models import AggregatedData

@app.route("/uav/<id>")
def get_uav1(id):
    response = {}
    try:

        uav_data = db.session.query(AggregatedData).filter(AggregatedData.topic.startswith(f"uav{id}/")).order_by(AggregatedData.timestamp.desc()).limit(11).all()
    except LookupError as e:
        abort(404)
    for el in AggregatedData.serialize_list(uav_data):
        response[el["topic"]] = el["value"]

    return response