# using () with re.findall to extract from the line only what we want:

import re

fhand = open('mbox-short.txt')

kount = 0

total = 0

for a in fhand:
    a = a.rstrip()
    x = re.findall('^X-\S*C\S*: ([0-9.]+)', a)
    if len(x) > 0:
        print(x)
        y = float(x[0])
        total += y
        kount += 1

print(kount)

avg = total / kount

print('average: %.4f' % avg)

fhand.close()