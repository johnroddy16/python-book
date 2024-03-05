# 8-10 from p4e, parsing lines:

fhand = open('mbox-short.txt')

kount = 0 

for a in fhand:
    a = a.rstrip()
    if not a.startswith('From '): continue
    # print(a)
    b = a.split()
    c = b[2]
    print(c)
    kount += 1
    

print()
print(kount)