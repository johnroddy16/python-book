# strings in python:

word = 'letter'
word += 's'

# print(word)

# using .find() and other methods on strings:

print()

ps = '    This / is a / good / string / 2 practice On    '

x = ps.split()

for a in x:
    try:
        a = int(a)
        print(a)
    except:
        continue

# print(x)
print()
y = ps.strip()
# print(y)
print(len(ps), len(y))
print()

z = y.find('/', 6)  # will return -1 if it does not find anything
print(z)
print()

# print(dir(y))
# print()