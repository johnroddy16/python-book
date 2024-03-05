# dsu, decorate, sort, undecorate:

# sort a list of words from longest to shortest:

text = 'but soft what light in yonder window breaks'

t = text.split()

v = []  # could also write v = list()

for a in t:
    v.append((len(a), a))

# print(v)

# print(type(v[0]))

v.sort(reverse=True)

h = []

for a, b in v:
    h.append(b)

print(h)