# tuples as dictionary keys:

directory = {}

directory['roddy', 'michael'] = 2064188234

print(directory)

last = 'coombs'

first = 'benjamin'


number = 2064444444

directory[last, first] = number

print(directory)

for a, b in directory:
    print('first: %s, last: %s, number: %d' % (b, a, directory[a, b]))