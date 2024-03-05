# the period as a character in re, remember the period represents any character, including space character:

import re

# search 4 lines that start with From and have an @ sign:

fhand = open('mbox-short.txt')

for a in fhand:
    a = a.rstrip()
    if re.search('F..m: .+@', a):  # lines that start with F..m:, then one or more of any char (.+), then an @ sign
        print(a)                   # .* would indicate 0 or more characters of any kind