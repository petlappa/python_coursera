import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter URL: ')
if len(url) < 1:
#    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
    url = 'http://py4e-data.dr-chuck.net/comments_106101.json'

print('Retrieving ',url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
#print(json.dumps(info, indent = 2))
print('User count:', len(info['comments']))
total = 0
for item in info['comments']:
    total = total + item['count']
#    print('Name', item['name'])
#    print('Count', item['count'])
print('Sum: ', total)
