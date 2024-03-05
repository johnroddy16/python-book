# readin binary files using urllib:

# http://data.pr4e.org

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()

fhand = open('cover3.jpg', 'wb')  # wb opens a binary file for writing only

fhand.write(img)


fhand.close()

# receiving data in blocks, or buffers, is a way to ensure your computer does not crash while retrieving,
# we can write to disk a bit of data at a time