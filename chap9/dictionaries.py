# practice with dictionaries:

name_age = {}

name_age['michael'] = 38

for a in name_age:
    print(a, name_age[a])

print(name_age)

names = ['jason', 'erik', 'matthew', 'pepper', 'xavier', 'juan']

name_and_num = {
    'michael': 206_418_8234,
    'kevin': 9072284934,
    'carolyn': 2062954876,
    'mom': 2063567535,
    'juan': 2063802424,
}

print(name_and_num)

print()

for n in names:
    if n in name_and_num:
        print('name: %s, number: %d' % (n, name_and_num[n]))