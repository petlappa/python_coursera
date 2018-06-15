# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if url == '' :
    #test file
#    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
    #prod file
    url = 'http://py4e-data.dr-chuck.net/known_by_Arzoo.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = input('Enter count: ')
if count == '' :
    count = 7
position = input('Enter position: ')
if position == '' :
    position = 18

# Retrieve all of the anchor tags
    while (count) :
#        print('count', count)
        count = count - 1
        pos_count = 0
        tags = soup('a')
        for tag in tags:
#            print('pos_count', pos_count)
            pos_count = pos_count + 1
#            print(tag.get('href', None))
            if pos_count == position :
#                print('pos 3')
                url = tag.get('href', None)
                print(tag.get('href', None))
                html = urllib.request.urlopen(url, context=ctx).read()
                soup = BeautifulSoup(html, 'html.parser')
                break
print('Done!')
