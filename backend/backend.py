from flask import Flask 
from flask_cors import CORS
from flask_pymongo import PyMongo 


import requests
import json
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/xlab"
mongo = PyMongo(app)
CORS(app)

@app.route("/")
def test():
  get_pothole()
  for doc in mongo.db.xlab.find():
    print(doc)
  result = {"passed": True}
  json_result = json.dumps(result)
  return json_result


@app.route("/total_score")
def get_total_score():
  pass

@app.route("/scores")
def get_topic_scores():
  pass



def get_pothole():
  url = "https://chelseama.ogopendata.com/datastore/odata3.0/50fd4973-d1c9-4897-8b7d-092a87ebc23b?&$format=json"
  r = requests.get(url)
  data = r.json()
  potholes = data['value']
  scores = []
  for row in potholes:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7 and row['Category'] == 'Pothole'):
      scores.append(1)
    else:
      scores.append(0)
  pothole_score = (sum(scores) / len(scores))
  mongo.db.xlab.insert({'pothole': pothole_score})


