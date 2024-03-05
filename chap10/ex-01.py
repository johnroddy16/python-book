# extracting and parsing data from mbox.txt and mbox-short.txt:

fhand = open('mbox.txt')

email_dict = {}

for a in fhand:
    a = a.split()
    if len(a) < 2 or a[0] != 'From': continue
    email_dict[a[1]] = email_dict.get(a[1], 0) + 1

# print(email_dict)

y = sorted([(b, a) for a, b in email_dict.items()], reverse=True)

for a, b in y[:1]:
    print(b, a)