# program that will read thru email data, extract the email address, and count how many emails came from the address:

fhand = open('mbox-short.txt')

email_count = {}

for a in fhand:
    a = a.split()
    if len(a) < 2 or a[0] != 'From': continue
    email_count[a[1]] = email_count.get(a[1], 0) + 1

y = sorted([(b, a) for a, b in email_count.items()], reverse=True)

for a, b in y:
    print('email: %s, count: %d' % (b, a))

fhand.close()

counts = list(email_count.values())

x = max(counts)
print(x)

for a in email_count:
    if email_count[a] == x:
        print(a, email_count[a])