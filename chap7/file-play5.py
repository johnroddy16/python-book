# more fun with mbox and mbox-short:

fhand = open('mbox-short.txt')

print()

for a in fhand:
    a = a.rstrip()
    if not a.startswith('From: '): continue
    print(a)

print()

fhand.close()