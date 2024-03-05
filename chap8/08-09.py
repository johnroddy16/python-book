# lists and strings:

b = 'banana'

c = list(b)

print(c)

delim = '/'

y = delim.join(c)
print(y)

s = 'john?kevin?michael?jayne'
d = '?'
t = s.split(d)
print(t)