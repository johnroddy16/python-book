# practicing with the file mbox-short.txt:

fhand = open('mbox-short.txt')

kount = 0

for a in fhand:
    kount += 1

print('total lines:', kount)

fhand.close()