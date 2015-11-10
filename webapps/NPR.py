import requests
from json import load

url = 'http://api.npr.org/query?apiKey='
key = 'API_KEY'
url = url + key
url += '&numResults=3&format=json&id='
url += raw_input("Which NPR ID do you want to query?")

response = requests.get(url)
json_obj = load(response.text)

print json_obj

#for story in json_obj['list']['story']:
#	print story['title']['$text']
