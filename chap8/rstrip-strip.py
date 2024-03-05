# trying strip and rstrip:

fhand = open('mbox-short.txt')

kount = 0

for a in fhand:
    a = a.rstrip()  # strip will take away all whitespace while rstrip will take away \n, including blank lines
    if kount < 10:  # lstrip leaves the \n and blank lines but eliminates whitespace at start of lines
        print(kount, a)
    if kount == 9:
        break
    kount += 1

print(kount)