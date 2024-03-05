# find the most common words in romeo-full.txt:

import string  # import string so we can eliminate punctuation

fhand = open('romeo-full.txt')

word_count = {}  # could also write word_count = dict()

for a in fhand:
    a = a.strip()
    a = a.translate(str.maketrans('', '', string.punctuation))
    a = a.lower()
    t = a.split()
    for w in t:
        word_count[w] = word_count.get(w, 0) + 1

y = sorted([(b, a) for a, b in word_count.items()], reverse=True)

for a, b in y[:25]:
    print('word: %s, count: %d' % (b, a))