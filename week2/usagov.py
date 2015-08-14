import json
import requests

response = requests.get("http://www.compjour.org/files/code/json-examples/analyticsgov-realtime.json")
data = json.loads(response.text)
print (response.text)
print('A.', data['name'])
print('B.', data['taken_at'])
print('C.', data['meta']['name'])
print('D.', data['data'][0]['active_visitors'])
print('E.', ',' .join(data.keys()))
#print (data.keys())
