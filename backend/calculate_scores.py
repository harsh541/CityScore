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


# click fix
url = "https://chelseama.ogopendata.com/datastore/odata3.0/50fd4973-d1c9-4897-8b7d-092a87ebc23b?&$top=5000000&$format=json"
r = requests.get(url)
clickFix = r.json()

def other_scores():
  other = [row for row in clickFix['value'] if "other" in row['Category'].lower()]

  for row in other:
    if (row['Closed Date'] is not None):
       row['Closed Date'] = datetime.strptime(row['Closed Date'], '%m/%d/%Y')
    else:
      row = None
  scores_year = []
  other_year = [row for row in other if (row['Closed Date'] is not None and row['Closed Date'].year == currentYear)]

  for row in other_year:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_year.append(1)
    else:
      scores_year.append(0)

  other_month = [row for row in other if (row['Closed Date'] is not None and row['Closed Date'].month == currentMonth - 1)]
  scores_month = []
  for row in other_month:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_month.append(1)
    else:
      scores_month.append(0)

  scores_day = []
  for index in range(len(other_month) - 3, len(other_month)):
    row = other_month[index]
    if (closed_days < 7):
      scores_day.append(1)
    else:
      scores_day.append(0)

  other_score_year = round(sum(scores_year) / len(scores_year), 3)
  other_score_month = round(sum(scores_month) / len(scores_month), 3)
  other_score_day = round(sum(scores_day) / len(scores_day), 3)

  return ("All Fix On Time %", other_score_day, other_score_month, other_score_year)

def graffiti_scores():

  graffiti = [row for row in clickFix['value'] if "graffiti" in row['Category'].lower()]

  for row in graffiti:
    if (row['Closed Date'] is not None):
      row['Closed Date'] = datetime.strptime(row['Closed Date'], '%m/%d/%Y')
    else:
      row = None
  
  scores_year = []
  graffiti_year = [row for row in graffiti if (row['Closed Date'] is not None and row['Closed Date'].year == currentYear)]

  for row in graffiti_year:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_year.append(1)
    else:
      scores_year.append(0)
  
  scores_month = []
  graffiti_month = [row for row in graffiti if (row['Closed Date'] is not None and row['Closed Date'].month == currentMonth - 1)]

  for row in graffiti_year:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_month.append(1)
    else:
      scores_month.append(0)

  scores_day = []
  
  for index in range(len(graffiti_month) - 3, len(graffiti_month)):
    row = graffiti_month[index]
    closed_days = float(row['Days to Closed'])
    if (closed_days < 14):
      scores_day.append(1)
    else:
      scores_day.append(0)
  
  graffiti_score_year = round(sum(scores_year) / len(scores_year), 3)
  graffiti_score_month = round(sum(scores_month) / len(scores_month), 3)
  graffiti_score_day = round(sum(scores_day) / len(scores_day), 3)

  # print("Graffiti On Time %", graffiti_score_day, graffiti_score_month, graffiti_score_year)

  return ("Graffiti On Time %", graffiti_score_day, graffiti_score_month, graffiti_score_year)

  
    

def street_light_scores():
  
  street_lights = [row for row in clickFix['value'] if "street light" in row['Category'].lower()]

  for row in street_lights:
    if (row['Closed Date'] is not None):
      row['Closed Date'] = datetime.strptime(row['Closed Date'], '%m/%d/%Y')
    else:
      row = None
  
  scores_year = []
  street_light_year = [row for row in street_lights if (row['Closed Date'] is not None and row['Closed Date'].year == currentYear)]

  for row in street_light_year:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 14):
      scores_year.append(1)
    else:
      scores_year.append(0)
  
  scores_month = []
  street_light_month = [row for row in street_lights if (row['Closed Date'] is not None and row['Closed Date'].month == currentMonth - 1)]

  for row in street_light_month:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 14):
      scores_month.append(1)
    else:
      scores_month.append(0)
  
  scores_day = []
  for index in range(len(street_light_month) - 3, len(street_light_month)):
    row = street_light_month[index]
    closed_days = float(row['Days to Closed'])
    if (closed_days < 14):
      scores_day.append(1)
    else:
      scores_day.append(0)

  street_light_score_year = round(sum(scores_year) / len(scores_year), 3)
  street_light_score_month = round(sum(scores_month) / len(scores_month), 3)
  street_light_score_day = round(sum(scores_day) / len(scores_day), 3)

  return ("Street Light On Time %", street_light_score_day, street_light_score_month, street_light_score_year)

def trash_scores():

  trash = [row for row in clickFix['value'] if "trash" in row['Category'].lower()]
  
  for row in trash:
    if (row['Closed Date'] is not None):
      row['Closed Date'] = datetime.strptime(row['Closed Date'], '%m/%d/%Y')
    else:
      row = None
  scores_year = []
  trash_year = [row for row in trash if (row['Closed Date'] is not None and row['Closed Date'].year == currentYear)]
  for row in trash_year:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_year.append(1)
    else:
      scores_year.append(0)
  
  trash_month = [row for row in trash if (row['Closed Date'] is not None and row['Closed Date'].month == currentMonth - 1)]
  scores_month = []

  for row in trash_month:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_month.append(1)
    else:
      scores_month.append(0)

  scores_day = []
  for index in range(len(trash_month) - 3, len(trash_month)):
    row = trash_month[index]
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_day.append(1)
    else:
      scores_day.append(0)
  
  trash_score_year = round(sum(scores_year) / len(scores_year), 3)
  trash_score_month = round(sum(scores_month) / len(scores_month), 3)
  trash_score_day = round(sum(scores_day) / len(scores_day), 3)

  return ("Missed Trash On Time %", trash_score_day, trash_score_month, trash_score_year)



def pothole_scores():
  potholes = [row for row in clickFix['value'] if row['Category'] == 'Pothole']

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
  for index in range(len(potholes_month) - 5, len(potholes_month)):
    row = potholes_month[index]
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_day.append(1)
    else:
      scores_day.append(0)

  pothole_scores_year = round(sum(scores_year) / len(scores_year), 3)
  pothole_scores_month = round(sum(scores_month) / len(scores_month), 3)
  pothole_scores_day = round(sum(scores_day) / len(scores_day), 3)

  return ("Pothole On Time %", pothole_scores_day, pothole_scores_month, pothole_scores_year)


  # print("pothole year:", pothole_scores_year)
  # print("pothole month:", pothole_scores_month)
  # print("pothole day:", pothole_scores_day)
