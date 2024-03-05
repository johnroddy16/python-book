# minimalist email client, exercise 5, chapter 8 p4e book:

fname = input('enter file name: ')

try:
    fhand = open(fname)
except:
    print('file not found:', fname, '/exiting program now')
    exit()

kount = 0

for a in fhand:
    a = a.split()
    if len(a) < 2 or a[0] != 'From': continue
    print(a[1])
    kount += 1

print('there were %d lines in the file with %s as the first word' % (kount, 'From'))