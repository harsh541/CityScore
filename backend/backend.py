import requests
import json
import sqlite3
from sqlite3 import Error
from flask import Flask 
from flask_cors import CORS
from flask import g

DATABASE = 'scores.db'

app = Flask(__name__)
CORS(app)

def query_db(query, args=(), one=False):
  conn = sqlite3.connect(DATABASE)
  curr = conn.execute(query)
  rv = curr.fetchall()
  curr.close()
  return(rv[0] if rv else None) if one else rv

@app.route("/")
def get_all():
  result = []
  for row in query_db('select * from score_data'):
    (_id, date, topic, day, month, year) = row
    obj_data = {'id': _id, 'topic': topic, 'day':day, 'month': month, 'year': year}
    result.append(obj_data)

  data = json.dumps(result)
  return data





