# using the period as a special character, which matches any character:

import re

list = ['Ftom', 'from', 'From' 'F4om']

lst = []

for a in list:
    if re.search('^F.', a):
        lst.append(a)


for a in lst:
    print(a, '\n')  # it prints funny