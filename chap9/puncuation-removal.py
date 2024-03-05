# removing puncuation and capitalization from romeo-full.txt in order to count accurately the number of different words used:

import string 

fname = input('enter file name: ')

try:
    fhand = open(fname)
except:
    print('file not found: %s, exiting program now' % fname)
    exit()

word_kount = {}

for a in fhand:
    a = a.strip()
    a = a.translate(a.maketrans('', '', string.punctuation))  # string.punctuation is a string
    a = a.lower()
    a = a.split()
    for w in a:
        word_kount[w] = word_kount.get(w, 0) + 1

y = sorted([(b, a) for a, b in word_kount.items()], reverse=True)

for a, b in y:
    print('word: %s, count: %d' % (b, a))

print(len(word_kount))

fhand.close()