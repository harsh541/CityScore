import requests

url = "https://chelseama.ogopendata.com/datastore/odata3.0/50fd4973-d1c9-4897-8b7d-092a87ebc23b"

headers = {
    'cache-control': "no-cache",
    'Postman-Token': "4eae3bf1-73af-452d-8fe0-9e24241725db"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
