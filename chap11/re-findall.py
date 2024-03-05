# re.findall practice:

# read thru a file and extract from each line anything that looks like an email:

import re

fhand = open('mbox.txt')

k = 0

for a in fhand:
    a = a.rstrip()
    x = re.findall('\S+@\S+', a)
    if len(x) > 0 and k < 100:
        print(f'{x}, {len(x)}')
        k += 1
    if k == 99:
        break

fhand.close()