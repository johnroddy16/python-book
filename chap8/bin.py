# binary:

x = bin(4)
y = bin(ord('4'))

print(x[2:], y[2:])

print(type(y))

z = int(y[2:])
print((z))