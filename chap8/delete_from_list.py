# different ways to remove or delete elements from a list:

ns = [4, 6, 7, 8]
ns.remove(6)
print(ns)
print()

ns.insert(1, 6)
print(ns)
print()

x = ns.pop(1)
print(x)
print()
print(ns)
print()

ns.insert(1, 6)
print(ns)
print()

y = ns.pop()  # will pop the last element
print(y)
print()

ns.append(y)
print(ns)
print()

del ns[1]
print(ns)
print()

del ns[1:]
print(ns)
print()