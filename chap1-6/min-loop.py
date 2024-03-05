# finding the smallest element in a list:

ns = [17, 4, 8, 2, 1.1, 1, 4.6, 7]

smallest = None

print('before:', smallest)
print()

for a in ns:
    if smallest == None or a < smallest:
        smallest = a
    print(a, smallest)

print()
print('after:', smallest)