import requests
import json
data_url = 'http://www.compjour.org/files/code/json-examples/single-tweet-librarycongress.json'
data = json.loads(requests.get(data_url).text)
#print(json.dumps(data, indent = 2))
print('A.',data['created_at'])
print('B.',data['user']['created_at'])
print('C.',data['text'])
print('D.',data['user']['screen_name'])
print('E.',data['id'])
print('F.',len(data['entities']['user_mentions']))
print('G.', ',' .join(a['text'] for a in data['entities']['hashtags']))
print('H.', ',' .join(a['display_url'] for a in data['entities']['urls']))
