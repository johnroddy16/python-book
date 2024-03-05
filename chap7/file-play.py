# practicing with the file mbox.txt:

fhand = open('mbox.txt')

# x = fhand.read()

kount = 0

for a in fhand:
    a = a.strip()
    if kount == 0:
        print(a)
    kount += 1

fhand.close()