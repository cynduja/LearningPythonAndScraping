import json
import requests

response = requests.get("http://www.compjour.org/files/code/json-examples/maps.googleapis-geocode-mcclatchy.json")
r = response.text
print(response.text)
data = json.loads(r)
print ("A.", data['checkins'])
print ("B.", data['likes'])
print ("C.", data['location']['longitude'])
print ("D.", data['category_list'][1]['name'])
