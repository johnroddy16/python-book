# exercise one from p4e book, chapter 12:
# for exercise two we will edit the program to stop retrieving after 3000 chars have been received:

# edit the program to allow user input for the url:

# the world's simplest web browser:           # http://data.pr4e.org/words.txt

# for exercise 5 we will edit the program to print only after the header:

import socket
import time

url = input('enter url: ')
try:
    x = url.split('/')
    z = x[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((z, 80))
    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()  # \r\n signifies an eol, back to back creates a blank line,
    mysock.send(cmd)                                                      # which we must send
    # print(type(mysock))  # class socket.socket                          # encode and b are equivalent
except:
    print('url not found: %s, exiting program now' % url)
    exit()

y = []

data_saved = ''

while sum(y) < 3000:
    data = mysock.recv(300)
    x = len(data)
    if x < 1: break
    time.sleep(.25)
    y.append(len(data))
    # print(x)
    data_saved += data.decode() 

c = data_saved.find('\r\n\r\n')

print(data_saved[c+4:])                                  # print(data.decode(), end='')

print(sum(y))

print()

print(c)

x = url.split('/')
z = x[2]
# print(z)

mysock.close()