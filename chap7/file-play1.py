# practicing with the file mbox-short.txt:

fhand = open('mbox-short.txt')

x = fhand.read()
print(len(x))

fhand.close()