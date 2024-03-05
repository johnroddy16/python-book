# practicing some with re:

import re 

text = ['From stephen@steve.net, fred@fred.net, and susan@susy.net']

for a in text:
    if re.search('^F..m .+@', a):
        print(a)