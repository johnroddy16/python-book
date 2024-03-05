# find lines that start with Deatails: http://....=39972

import re

# use re.findall and () to extract certain data from the lines:

fhand = open('mbox-short.txt')

kount = 0

for a in fhand:
    a = a.rstrip()
    x = re.findall('^De\S*: http\S*=([0-9]+)', a)  # [0-9]+ is greedy so will get as many numbers as possible
    if len(x) > 0:
        print(x)
        kount += 1

print(kount)

fhand.close()