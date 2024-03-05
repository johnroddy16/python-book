# let's just find the ones with host @uct.ac.za:

fhand = open('mbox-short.txt')

print()

for a in fhand:
    a = a.rstrip()
    if a.find('@uct.ac.za') == -1: continue  # if the string is not found within the string
    print(a)

print()

fhand.close()