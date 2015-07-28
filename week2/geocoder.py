import requests
import json
import sys

data_url = "http://www.compjour.org/files/code/json-examples/maps.googleapis-geocode-mcclatchy.json"
response = requests.get(data_url)
text = response.text
data = json.loads(text)
#print(data)

print('A.', data['results'][0]['formatted_address'])
print(sys.version)
print('B.', data['results'][0] ['geometry']['location_type'])
print('C.', data['status'])
print('D.', data['results'][0] ['geometry']['location']['lat'])
print('E.', data['results'][0] ['geometry']['viewport']['southwest'] ['lng'])
print('F.', ','.join(a['long_name'] for a in data['results'][0]['address_components'][0:2]))
