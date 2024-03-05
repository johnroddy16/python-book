# let's write the same program as binary-read.py but this time with some insurance code that will make sure
# our computer does not crash:

# readin binary files using urllib:

# http://data.pr4e.org

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')

fhand = open('cover4.jpg', 'wb')  # wb opens a binary file for writing only

size = 0

while True:
    info = img.read(100000)
    x = len(info)
    if x < 1: break
    size += len(info)
    fhand.write(info)

print('%d chars copied' % size)

fhand.close()

# receiving data in blocks, or buffers, is a way to ensure your computer does not crash while retrieving,
# we can write to disk a bit of data at a time