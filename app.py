from flask import Flask, render_template, jsonify

app = Flask(__name__)

DATA = [{
    "id": 1,
    "name": "Springfield Park",
    "location": "Cook, Illinois",
    "year_build": 1985
}, {
    "id": 2,
    "name": "Maple Ridge",
    "location": "Suffolk, Virginia",
    "year_build": 1998
}, {
    "id": 3,
    "name": "Oak Grove",
    "location": "Jackson, Missouri",
    "year_build": 2003
}, {
    "id": 4,
    "name": "Pine Creek",
    "location": "Erie, Pennsylvania",
    "year_build": 1976
}, {
    "id": 5,
    "name": "Willow Springs",
    "location": "Wake, North Carolina",
    "year_build": 2009
}, {
    "id": 6,
    "name": "Cedar Heights",
    "location": "Linn, Iowa",
    "year_build": 1989
}, {
    "id": 7,
    "name": "Cherry Valley",
    "location": "Winnebago, Illinois",
    "year_build": 1995
}, {
    "id": 8,
    "name": "Riverbend Estates",
    "location": "Cobb, Georgia",
    "year_build": 2001
}, {
    "id": 9,
    "name": "Meadowview Hills",
    "location": "Jefferson, Kentucky",
    "year_build": 1982
}, {
    "id": 10,
    "name": "Lakeview Terrace",
    "location": "Tulare, California",
}]


@app.route("/")
def homepage():
  return render_template('home.html', site_data=DATA)


@app.route("/data")
def list_data():
  return render_template('home.html', site_data=DATA)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
