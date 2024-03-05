# list arguments from p4e book, chapter 8, section 8-13:

def delete_head(t):  # this will modify the list
    del t[0]
    print(t)  

x = [2, 4, 6, 8]

delete_head(x)

print(x)


# without modifying the list:

def tail(t):
    print(t[1:])  # this will create a new object and leave the original unchanged

y = [4, 8, 16, 32]

tail(y)

print(y)