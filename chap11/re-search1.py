# re.search:

import re

fhand = open('mbox-short.txt')

kount = 0

for a in fhand:
    a = a.rstrip()
    if re.search('^X-\S*: [0-9.]+', a):
        print(a, type(a))
        kount += 1

print()
print(kount)

fhand.close()