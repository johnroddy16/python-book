# more fun with mbox and mbox-short:

print()

fhand = open('mbox-short.txt')

emails = 0

email_list = {}

for a in fhand:
    a = a.strip()
    if a.startswith('From: '):
        # print(a)
        x = a.find('@')
        y = a[x+1:]
        email_list[y] = email_list.get(y, 0) + 1
        emails += 1

print('total emails: %d' % emails)

print()

print(email_list)

print()

e = sorted([(b, a) for a, b in email_list.items()], reverse=True)

for a, b in e:
    print(f'email: {b}, number of times: {a}')

fhand.close()