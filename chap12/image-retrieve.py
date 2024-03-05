# retrieving an image over the web:

import socket
import time

host = 'data.pr4e.org'
port = 80

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, port))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')

kount = 0
picture = b''

while True:
    data = mysock.recv(5120)
    x = len(data)
    if x < 1: break
    time.sleep(.25)  # this creates flow control
    kount += x
    print(x, kount)
    picture += data

mysock.close()

# look 4 the end of the header:

pos = picture.find(b'\r\n\r\n')
print('header length: %d' % pos)
print(picture[:pos].decode())  # printing the header

# skip past the header and save the picture data:

picture = picture[pos+4:]
fhand = open('stuff.jpg', 'wb')
fhand.write(picture)
fhand.close()

# easy peasy