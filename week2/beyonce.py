import json
import requests

response = requests.get("http://www.compjour.org/files/code/json-examples/spotify-related-to-beyonce.json")
text = response.text
data = json.loads(text)
#print(json.dumps(data, indent=2))
print('A.', len(data['artists']))
print('B.', data['artists'][4]['name'])
print('C.', data['artists'][11]['followers']['total'])
print('D.', ',' .join(data['artists'][0]['genres']))
print('E.', data['artists'][-1]['images'][0]['url'])