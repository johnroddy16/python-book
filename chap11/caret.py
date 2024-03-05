# the ^ indicates that the line must start with the argument:

import re

fhand = open('mbox-short.txt')

kount = 0

for a in fhand:
    a = a.rstrip()
    if re.search('^From:', a):
        print(a)
        kount += 1

print(kount)