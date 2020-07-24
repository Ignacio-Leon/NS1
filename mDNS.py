from ns1 import NS1
from pprint import pprint
import json

api = NS1(apiKey='Cvr1rNn4nZkhgiyraLFh')

test_zone = api.loadZone('leonmarine.com')
pprint(test_zone.data)
for record in test_zone['records']:
    rr = test_zone.loadRecord(record['domain'],record['type'])
    pprint (rr.data)
#Monitors = api.config
#pprint (Monitors)

