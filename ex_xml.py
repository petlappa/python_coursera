import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

url = input('Enter URL: ')
if len(url) < 1:
#    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
    url = 'http://py4e-data.dr-chuck.net/comments_106100.xml'

print('Retrieving ',url)
xml = urllib.request.urlopen(url).read()
print('Retrieved', len(xml), 'characters')
tree = ET.fromstring(xml)
total = 0
counter = 0
#while True :
#print(tree)
lst = tree.findall('comments/comment')
print('Count: ', len(lst))
for item in lst:
    print('Count', item.find('count').text)
    total = total + int(item.find('count').text)
print('total', total)
