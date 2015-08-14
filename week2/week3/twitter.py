import requests
import json
import os
data_url = 'http://www.compjour.org/files/code/json-examples/twitter-cspan-congress-list.json'
tempfilename = "/tmp/congresslist.json"

if os.path.exists(tempfilename):
	tfile = open(tempfilename, "r")
	j = tfile.read()
else:
	response = requests.get(data_url)
	j = response.text
	tfile = open(tempfilename, "w")
	tfile.write(j)
tfile.close()
accounts = json.loads(j)
print (accounts)