# use urllib to make a program similar to socket1.py:

import urllib.request, urllib.parse, urllib.error    # http://data.pr4e.org/words.txt

url = input('enter url: ')
try:
    fhand = urllib.request.urlopen(url)
except:
    print('url not found: %s, exiting program now' % url)
    exit()

chars = 0

# y_x = 0

while True:
    x = fhand.read(1000).decode()  # this program will read 1000 chars at a time until no more data to retrieve,
    y = len(x)                     # and display up to 1000, 2000, 3000, etc chars, depending on how it is set
    if y < 1: break                # it is pretty cool
    # y_x += y
    if chars < 1000:
        print(x)
    chars += y

print(chars)
# print(y_x)

fhand.close()