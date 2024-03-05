# playing with words.txt:

fhand = open('words.txt')

word_dict = {}

for a in fhand:
    a = a.split()
    if len(a) < 1: continue
    # print(a)
    for w in a:
        w = w.lower()
        if w.endswith(','):
            w = w[:-1]
        word_dict[w] = word_dict.get(w, 0) + 1

# for a, b in word_dict.items():
#     print(a, b)

y = sorted([(b, a) for a, b in word_dict.items()], reverse=True)

kount = 1

for a, b in y[:10]:
    print('%d %s %d times' % (kount, b, a))
    kount += 1

x = 'Program' in word_dict
print(x)