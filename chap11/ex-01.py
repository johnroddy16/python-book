# write a program that simulates the grep command in Unix:

import re

# generalized regular expression parser:

# in the terminal, grep '^From:' mbox-short.txt would return lines that start with From: and contain email addresses
# in grep, [^ ] replaces \S as the ^ inverts the meaning and will search for any non-whitespace character

fhand = open('mbox-short.txt')

for a in fhand:
    a = a.rstrip()
    