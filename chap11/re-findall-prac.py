# re.findall practice:

# re.findall searches a string and creates a list of all that matches the regular exoression:

import re 

fhand = open('mbox.txt')

spam = 0

instances = 0

lines = 0

# this is not the best way to do this as re.findall creates a list:

for a in fhand:  # looking for this: ['X-DSPAM-Probability: 0.0000']
    a = a.rstrip()
    x = re.findall('.*SPAM.*C.*', a)
    if len(x) > 0:
        y = str(x)
        z = y.split(':')
        g = z[1]
        h = float(g[:-2])
        spam += h
        instances += 1

average = spam / instances

print(spam, instances)

print('%.2f' % average)

fhand.close() 