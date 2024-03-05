# unique words in romeo.txt:

fhand = open('romeo.txt')

unique_words = []

for a in fhand:
    t = a.split()
    if len(t) < 1: continue
    for w in t:
        if w not in unique_words:
            try:
                d = w.lower()
                unique_words.append(d)
            except:
                unique_words.append(w)

unique_words.sort()

print(unique_words, '\n', len(unique_words))

fhand.close()