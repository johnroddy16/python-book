# dictionaries and tuples, the ultimate combination:

lets = {'a': 1, 'b': 2, 'd': 4, 'c': 3}

t = list(lets.items())

t.sort()  # sort by key

print(t)

for a, b in lets.items():
    print(a, b)