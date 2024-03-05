# editing urllinks.py to find the p tags:


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

p_kount = 0

tags = soup('p')

print(type(tags[0]))  # <class 'bs4.element.Tag'>

# print(tags)

print()

for t in tags:
    # print(t)
    print(t.get('class', None))
    p_kount += 1

print(p_kount)

print()

print(type(tags))

# https://docs.python.org