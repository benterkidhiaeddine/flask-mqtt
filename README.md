# flask-mqtt
Integrate mqtt into a flask application
Installation steps:
```
python -m venv venv
venv\Scripts\activate
pip install -r requiremnts.txt
python app.py
flask db migrate
flask upgrade
```
schema returned by route "/uav/id" where id can 1 or 2  for different uavs:
```
{
  "uav1/armed": "1",
  "uav1/bat/id": "1",
  "uav1/bat/pt": "1.0",
  "uav1/bat/vl": "16.2",
  "uav1/gps/abs": "116.07125854492188",
  "uav1/gps/fx": "3",
  "uav1/gps/lat": "-8.75313944210458",
  "uav1/gps/lon": "115.47149481353811",
  "uav1/gps/ns": "10",
  "uav1/in_air": "False",
  "uav1/state": "4"
}
```
