# combining searching and extracting:

import re 

# select some lines using brackets:

fhand = open('mbox-short.txt')

for a in fhand:
    a = a.rstrip()
    x = re.findall('^X-.*: [0-9.]+', a)
    if len(x) > 0:
        print(x)

fhand.close()
# with ^X-.*: [0-9.]+ we are looking for lines that start with X-, followed by 0 or more of any char, followed by :, followed by a space,
# followed by either a number 0-9 or a ., at least one