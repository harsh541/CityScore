import requests
import sqlalchemy as db

from datetime import datetime
 
# getting current date and time, this is in UTC format
d = datetime.today()

# getting current year
currentYear = d.year
 
#getting current month
currentMonth = d.month
 
#getting current day
currentDay = d.day


def pothole_scores():
  url = "https://chelseama.ogopendata.com/datastore/odata3.0/50fd4973-d1c9-4897-8b7d-092a87ebc23b?&$top=5000000&$format=json"
  r = requests.get(url)
  data = r.json()
  #print(data)
  potholes = [row for row in data['value'] if row['Category'] == 'Pothole']

  for row in potholes:
    if (row['Closed Date'] is not None):
      row['Closed Date'] = datetime.strptime(row['Closed Date'], '%m/%d/%Y')
    else:
      row = None

  # gets the pothole incidents with year 2019
  scores_year = []
  potholes_year = [row for row in potholes if (row['Closed Date'] is not None and row['Closed Date'].year == currentYear)]
  for row in potholes_year:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_year.append(1)
    else:
      scores_year.append(0)


  potholes_month = [row for row in potholes if (row['Closed Date'] is not None and row['Closed Date'].month == currentMonth - 1)]
  scores_month = []
  for row in potholes_month:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_month.append(1)
    else:
      scores_month.append(0)

  scores_day = []
  for index in range(len(potholes_month) - 3, len(potholes_month)):
    row = potholes_month[index]
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_day.append(1)
    else:
      scores_day.append(0)

  pothole_scores_year = round(sum(scores_year) / len(scores_year), 3)
  pothole_scores_month = round(sum(scores_month) / len(scores_month), 3)
  pothole_scores_day = round(sum(scores_day) / len(scores_day), 3)

  return (pothole_scores_day, pothole_scores_month, pothole_scores_year)


  # print("pothole year:", pothole_scores_year)
  # print("pothole month:", pothole_scores_month)
  # print("pothole day:", pothole_scores_day)
