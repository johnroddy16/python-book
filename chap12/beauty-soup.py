# beautiful soup:

# we will use beautiful soup and urllib to attack the web:

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('enter url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all of the anchor tags:

tags = soup('a')
# print(tags)
print()
for t in tags:
    # print(t)
    print(t.get('href', None))
print()
print(type(tags))

# https://docs.python.org