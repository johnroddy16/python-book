# search with re.findall for lines that start with From and extract the time of day:

import re

fhand = open('mbox-short.txt')

kount = 0

for a in fhand:
    a = a.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', a) # original code I wrote: ^From.*[0-9]* ([0-9]+:[0-9]+:[0-9]+) 
    if len(x) > 0:                                             # other ode is from p4e book
        print(x)
        kount += 1

print(kount)

fhand.close()