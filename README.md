# flask-mqtt
Integrate mqtt into a flask application
Installation steps:
1. Create a python virtual environement
- for a windows machine use the following:
```
python -m venv venv
```
- for a linux machine use the following:
```
python3 -m venv venv
```
2. Activate the virutal environment 
- for a windows machine use the following:
```
venv\Scripts\activate 
```
- for a linux machine use the following:
```
source venv/bin/activate
```
3. Do migrations for the database using the following command : make sure your .flaskenv is present and FLASK_APP points to the file containing your flask app
```
flask db migrate
```
4. Apply the migrations in the database 
```
flask upgrade
```
4. Launch the app with the developement server : it will be exposed on localhost:5000
```
python app.py
```
5. The schema of the data returned by the routes:

- schema returned by route "/uav/id" where id can 1 or 2  for different uavs:
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
