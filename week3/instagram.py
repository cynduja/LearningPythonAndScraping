import requests
import json 
from collections import Counter
from operator import itemgetter
response = requests.get("http://www.compjour.org/files/code/json-examples/instagram-aaron-schock.json")
text = response.text
data = json.loads(text)
instagram = data['data']
print len(instagram)
ix=len([i for i in instagram if i['type'] == "image"])
vx = len([i for i in instagram if i['type'] == "video"])
print "A.",ix,"|", vx 
filters = [i['filter'] for i in instagram if i['filter']]
c = Counter(filters)
# top3 = c.most_common(3)
# print top3
filter_list = list(c.items())
top3 = sorted(filter_list, key = itemgetter(1),reverse=True)[0:3]

top3_strs = []
for t in top3:
    x = str(t[0]) + ':' + str(t[1])
    top3_strs.append(x)

located_items = [i for i in instagram if i['location']]
geocoded_items = [i for i in located_items if i['location'].get('latitude')]
print "C.", len(geocoded_items)

capitol_items = [i for i in located_items if i['location'].get('name') == "United States Capitol"]
print "D.", len(capitol_items)

location_name_list = [g['location'].get('name') for g in geocoded_items]

c = Counter(location_name_list)
top3 = c.most_common(3)
top3_strs = []
for t in top3:
    x = str(t[0]) + ':' + str(t[1])
    top3_strs.append(x)

print "E.",("|").join(top3_strs)

def sum_likes_comments(i):
	return i['likes']['count'] + i['comments'].get('count')

highest_count = max(instagram, key = sum_likes_comments)

print'G.', '|'.join([i['caption']['text'][0:19],
  i['images']['thumbnail']['url'],
  str(i['likes']['count']),
  str(i['comments']['count'])
])

import time
oldest = max([i['created_time'] for i in instagram]
)
newest = min([i['created_time'] for i in instagram])
span_days = (int(oldest) - int(newest))/(60*60*24)
print "H.", round(span_days)
