# Bring in the library
import requests
import json
# make the GET call
resp = requests.get("http://www.example.com")
print(type(resp))  # => <class 'requests.models.Response'>
txt = resp.text
# print the size of the webpage's content:
print(len(txt))  # => 1270
resp = requests.get("https://status.github.com/api/status.json")
x = resp.json()
print(x)
print("Github's status is currently:", x['status'], 'as of:', x['last_updated'])

