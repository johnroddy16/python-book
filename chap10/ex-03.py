# letter frequency:

import string 

fname = input('enter file name: ')
try:
    fhand = open(fname)
except:
    print('file not found: %s, exiting program now' % fname)
    exit()

letters = {}

alpha = 'abcdefghijklmnopqrstuvwxyz'

for a in fhand:  # could write this program with a = a.translate(a.maketrans('', '', string.punctuation))
    a = a.lower()
    a = a.strip()
    for l in a:
        if l not in alpha: continue
        letters[l] = letters.get(l, 0) + 1

y = sorted([(b, a) for a, b in letters.items()], reverse=True)

print(len(letters))

total = sum(list(letters.values()))

print(total)

for a, b in y:
    print('letter: %s, count: %d, percentage: %.2f' % (b, a, a / total * 100))