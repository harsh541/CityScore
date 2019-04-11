import requests
url = "https://chelseama.ogopendata.com/datastore/odata3.0/50fd4973-d1c9-4897-8b7d-092a87ebc23b?&$format=json"
r = requests.get(url)
data = r.json()
print(data)
potholes = data['value']
scores = []
for row in potholes:
 closed_days = float(row['Days to Closed'])
 if (closed_days < 7 and row['Category'] == 'Pothole'):
   scores.append(1)
 else:
   scores.append(0)

pothole_score = (sum(scores) / len(scores))
print('pothole score', pothole_score)