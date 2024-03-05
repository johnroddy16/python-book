# regular expressions are very cool, a simple example:

import re

fhand = open('mbox-short.txt')

kount = 0

for a in fhand:
    a = a.strip()
    if re.search('From:', a):
        print(a)
        kount += 1

print(kount)