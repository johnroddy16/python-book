# using re.findall to look for lines with email addresses and then take only the part of the address we want:

import re

fhand = open('mbox-short.txt')

# [] are used to indicate a set of characters we are willing to accept:

line = 0

for a in fhand:
    a = a.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', a)  # [a-zA-Z0-9], [a-zA-Z], 335 ['wagnermr@iupui.edu']
    if len(x) > 0:  # must start with something in brackets and end with something in brackets 
        print(line, x)
        line += 1