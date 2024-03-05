# sort a tuple by creating a new one:

x = (4, 8, 4, 6, 9, 1, 0, 3)

y = tuple(sorted(x))  # sorted alone will create a list, which we may sometimes want
print(y)

z = tuple(reversed(y))  # should use tuple or list or we will get back a hex memory address
print(z)