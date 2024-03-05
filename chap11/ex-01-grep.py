# write a program that simulates the grep command in Unix:

import re

# generalized regular expression parser:

# in the terminal, grep '^From:' mbox-short.txt would return lines that start with From: and contain email addresses
# in grep, [^ ] replaces \S as the ^ inverts the meaning and will search for any non-whitespace character

r_e = input('enter regualr expression: ')

fhand = open('mbox.txt')

kount = 0

for a in fhand:
    a = a.rstrip()
    if re.search(r_e, a):
        # print(a)
        kount += 1

print('mbox.txt had %d lines that matched %s' % (kount, r_e))

fhand.close()