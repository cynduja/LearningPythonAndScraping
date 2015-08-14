import csv
import os.path
DATA_DIR = "data-hold"
csvname = os.path.join (DATA_DIR, 'sunlight_legislators.csv')
csvdata = csv.DictReader(open(csvname, encoding = 'utf-8'))
print (csvdata)
congressmembers = []
for row in csvdata:
	congressmembers.append(row)
#print (congressmembers)

print("There are {} Congressmembers listed".format(len(congressmembers)))

#Active members:

active_members = []

for m in congressmembers:
	if m['in_office'] == '1':
		active_members.append(m)
print("There are {} active Congressmembers".format(len(active_members)))
#print (active_members)

# Now we want active members who are in California

ca_active_members = []
for m in active_members:
    if m['state'] == 'CA':
        ca_active_members.append(m)
print("There are {} active Congressmembers from CA".format(len(ca_active_members)))

ca_tweeters = [m for m in ca_active_members if m['twitter_id'] != '']
print("There are {} active CA Congressmembers from CA on Twitter".format(len(ca_tweeters)))