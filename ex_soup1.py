# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if url == '' :
    url = 'http://py4e-data.dr-chuck.net/comments_106098.html'
#     url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
nlist = []

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
#    print('TAG:', tag)
    print('TAG.text:',tag.text)  # It is the tag.text we need to scan for integers.
    for x in re.findall('[0-9]+', tag.text):
        nlist.append(int(x))
#print (nlist)
total = 0
for i in nlist :
    total = total + i
print (total)
