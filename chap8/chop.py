# exercise one from p4e book, chapter 8:

def chop(t):  # remove the first and last elements from a list
    del t[0]
    del t[-1]

x = [16, 32, 64, 128]

chop(x)

print(x)

def middle(t):  # create a new list with the middle elements from argument list
    y = t[1:-1]
    return y

z = [4, 8, 16, 32, 64, 128, 256, 512]

a = middle(z)

print(a)
print(z)