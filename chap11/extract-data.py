# using re to extract data:

import re

# we can use re.findall() to extract data from a string:

s = 'a message from john.roddy.18@phys.org to micheal.r.64@golf.org about a meeting @4p'

print(s)
print()

lst = re.findall('\S+@\S+', s)  #\S matches as many non-whitespace chars as possible, it is pretty cool

print(lst)