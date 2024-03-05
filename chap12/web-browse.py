# the world's simplest web browser:

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = b'GET http://data.pr4e.org/words.txt HTTP/1.0\r\n\r\n'#.encode()  # \r\n signifies an eol, back to back creates a blank line,
mysock.send(cmd)                                                      # which we must send
# print(type(mysock))  # class socket.socket                          # encode and b are equivalent
y = []

while True:
    data = mysock.recv(512)
    x = len(data)
    if x < 1: break
    y.append(len(data))
    print(data.decode(), end='')

print(y)

mysock.close()