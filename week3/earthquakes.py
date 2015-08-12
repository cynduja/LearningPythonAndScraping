import requests
import json
import os
from operator import itemgetter 

data_url = "http://www.compjour.org/files/code/json-examples/earthquake.usgs-significant_month.json"
response = requests.get(data_url)
text = response.text
data = json.loads(text)

f=open('earthquakes.json', "w")
f.write(json.dumps(data, indent=2))
f.close()

print('A.', data['metadata']['title'])

print('B.', len(data['features']))

quakes = data['features']
x = max(q['properties']['mag'] for q in quakes)
print('C.',x)

totes=0

for q in quakes:
	if q['properties']['tsunami']==1:
		totes = totes+1
print ('D.',totes)


def get_mag(quakes):
	return quakes['properties']['mag']

z=min(quakes, key=get_mag)
print('E.', z['properties']['title'])

def get_felt(quakes):
	return quakes['properties']['felt']

z=max(quakes, key=get_felt)
print('F.', z['properties']['title'])

import time

qsecs = [q['properties']['time']/1000 for q in quakes]
qsecs = sorted(qsecs, reverse=True)
tsec = qsecs[0]
timeobj = time.gmtime(tsec)
#print (timeobj)
print('G.', time.strftime('%Y-%m-%d %H:%M', timeobj) )

osec = qsecs[-1]
timeobj = time.gmtime(osec)
print('H.',time.strftime('%A,%B %d', timeobj))

weekend = ['Saturday', 'Sunday']
i=0
for q in qsecs:
	timeobj = time.gmtime(q)
	day = time.strftime('%A', timeobj)
	if day not in weekend:
		i = i+1
print ('I.', i)


basemap_url = 'https://maps.googleapis.com/maps/api/staticmap?zoom=1&size=500x400'
markers_str = 'markers=color:orange'
for q in quakes:
    coords = q['geometry']['coordinates']
    lng = str(coords[0])
    lat = str(coords[1])
    s = '%7C' + lat + ',' + lng
    markers_str += s

print('M.', basemap_url + '&' + markers_str)  


# Task N
orange_str = 'markers=color:orange'
red_str = 'markers=color:red'

for q in quakes:
    coords = q['geometry']['coordinates']
    lng = str(coords[0])
    lat = str(coords[1])
    s = '%7C' + lat + ',' + lng

    if q['properties']['mag'] >= 6:
        red_str += s
    else:
        orange_str += s

print('N.', basemap_url + '&' + orange_str + '&' + red_str)

# Task K
from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat /2 ) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers.
    return c * r

def distance_from_stanford(quake):
    stanford_lng = -122.166
    stanford_lat = 37.424
    coords = quake['geometry']['coordinates']
    lng = coords[0]
    lat = coords[1]
    return haversine(lng, lat, stanford_lng, stanford_lat)

q = max(quakes, key = distance_from_stanford)
print('K.', q['properties']['title'])

#########################
# Task L
# assuming haversine has been defined as above
def d_paris(quake):
    paris_lng = -0.8655079
    paris_lat = 44.562918
    coords = quake['geometry']['coordinates']
    lng = coords[0]
    lat = coords[1]
    return haversine(lng, lat, paris_lng, paris_lat)

q = max(quakes, key = d_paris)
print('L.', q['properties']['title'])
