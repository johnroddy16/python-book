# write a program that looks for lines of the form:

import re

fname = input('enter file name: ')

try:
    fhand = open(fname)
except:
    print('file not found: %s, exiting program now' % fname)
    exit()

kount = 0

total = 0

for a in fhand:
    a = a.rstrip()
    x = re.findall('^New R.*: ([0-9]+)', a)
    if len(x) > 0:
        # print(x)
        y = int(x[0])
        # print(y)
        total += y
        kount += 1

print(kount)

avg = int(total / kount)

print(avg)

fhand.close()