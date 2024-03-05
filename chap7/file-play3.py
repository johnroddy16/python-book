# practicing with the file mbox-short.txt and mbox.txt:

print()

fhand = open('mbox.txt')

letter_dict = {}

r = fhand.read().lower()

r.replace(' ', '')

total = 0

for l in r:
    if l not in 'abcdefghijklmnopqrstuvwxyz': continue 
    letter_dict[l] = letter_dict.get(l, 0) + 1
    total += 1

y = sorted([(b, a) for a, b in letter_dict.items()], reverse = True)

print(len(letter_dict))

print()

for a, b in y:
    d = a / total
    p = d * 100
    print('letter: %c times: %d percentage %.2f%s' % (b, a, p, '%'))  # %c or %s will work for a character, only %s for a string

print()

fhand.close()