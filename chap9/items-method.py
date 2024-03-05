# playing with .items() and dictionaries:

word = 'brontosaurus'

letters = dict()

for l in word:
    if l not in letters:
        letters[l] = 1
    else:
        letters[l] += 1

# same thing but with .items():

lets = {}

for a in word:
    lets[a] = lets.get(a, 0) + 1

print(letters)
print()
print(lets)

print(letters is lets)  # different objects

print(hex(id(letters)), hex(id(lets)))  # pretty cool stuff