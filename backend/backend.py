import requests
import json
import requests
import os

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from calculate_scores import pothole_scores
from datetime import datetime

app = Flask(__name__)
CORS(app)
# db_path = os.path.join(os.path.dirname(__file__), 'xlab.db')
# db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class ScoreData(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.String(120), unique=False, nullable=False)
  topic = db.Column(db.String(120), unique=True, nullable=False)
  day = db.Column(db.Float, unique=False, nullable=True)
  month = db.Column(db.Float, unique=False, nullable=True)
  year = db.Column(db.Float, unique=False, nullable=True)

  def __init__(self, date, topic, day, month, year):
    self.date = date
    self.topic = topic
    self.day = day
    self.month = year
    self.year = year

def add_row():
  (pothole_day, pothole_month, pothole_year) = pothole_scores()
  pothole_score_data = ScoreData(datetime.now().strftime("%Y-%m-%d %H:%M"), 'does this work', pothole_day, pothole_month, pothole_year)
  db.session.add(pothole_score_data)
  db.session.commit()


@app.route("/")
def get_all():
  score_data = ScoreData.query.all()
  result = []
  for row in score_data:
    curr = {'id': row.id, 'topic': row.topic, 'day': row.day, 'month': row.month, 'year': row.year}
    result.append(curr)
  result2 = {"passed": True}
  json_result = json.dumps(result)
  print(result)
  return json_result



if __name__ == '__main__':
  # db.create_all()
  add_row()
  



