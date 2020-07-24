import requests
from pprint import pprint

API_KEY = "Cvr1rNn4nZkhgiyraLFh"
URL = 'https://api.nsone.net/v1/zones/leonmarine.com'
response = requests.get(URL,headers={'X-NSONE-Key': API_KEY})
data = response.json()
pprint (data)


