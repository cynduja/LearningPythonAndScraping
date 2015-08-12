import requests
import json
import os
from operator import itemgetter
data_url = 'http://www.compjour.org/files/code/json-examples/twitter-cspan-congress-list.json'
tempfilename = "/tmp/congresslist.json"
# if you're on Windows, do this:
# tempfilename = os.path.expandvars('%TEMP%\\congresslist.json')

# Because this file is relatively large, let's save it to a tempfile, so that
# subsequent runs read from that file
if os.path.exists(tempfilename):
    tfile = open(tempfilename, "r")
    j = tfile.read()
else:    
    j = requests.get(data_url).text
    tfile = open(tempfilename, "w")
    tfile.write(j)

tfile.close()
accounts = json.loads(j)
## woof, that was a lot of lines just to load a file...
f = open("congresslist.json", "w")
f.write(json.dumps(accounts, indent=2))
print('A.', len(accounts))

x=0
for a in accounts:
	if a['followers_count']>10000:
		x = x+1
print('B.', x)

x=0
for a in accounts:
	if a['verified']==True:
		x=x+1
print('C.', x)
'''
counts = []
for a in accounts:
	counts.append(a['followers_count'])
maxval = sorted(counts, reverse = True)[0]
print('D.', maxval)
'''
print('D.', max(a['followers_count'] for a in accounts))

print('E.', max(a['statuses_count'] for a in accounts))

x = max(accounts, key=itemgetter('followers_count'))
print('F.', x['screen_name'], 'has', x['followers_count'], 'followers')

count =[]
for a in accounts:
	if a['verified'] == False:
		count.append(a)
x = max(count, key=itemgetter('statuses_count'))
print('G.', x['screen_name'], 'has', x['statuses_count'])

totes = 0
for a in accounts:
	totes = totes + a['followers_count']
print ('H.', round(totes/len(accounts)))

z=sorted(accounts, key=itemgetter('followers_count'))
m=z[len(z)//2]
print('I.', m['followers_count'])
