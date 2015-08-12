import requests
import json 
response = requests.get("http://www.compjour.org/files/code/json-examples/instagram-aaron-schock.json")
text = response.text
data = json.loads(text)
instagram = data['data']
print len(instagram)
ix=len([i for i in instagram if i['type'] == "image"])
vx = len([i for i in instagram if i['type'] == "video"])
print "A.",ix,"|", vx 