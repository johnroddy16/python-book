# a dictionary that will contain days of the week count from email data:

fname = input('enter file name: ')

try:
    fhand = open(fname)
except:
    print('file not found: %s, exiting program now' % fname)
    exit()

days = dict()  # could write days = {}

for a in fhand:
    a = a.split()
    if len(a) < 3 or a[0] != 'From': continue
    days[a[2]] = days.get(a[2], 0) + 1

print(days)
print()

y = sorted([(b, a) for a, b in days.items()], reverse=True)

for a, b in y:
    print('day: %s, times: %d' % (b, a))

weekday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
weekend = ['Sat', 'Sun']

weekday_count = 0
weekend_count = 0
total = 0

for d in days:
    if d in weekday:
        weekday_count += days[d]
    else:
        weekend_count += days[d]
    total += days[d]

print('weekday emails: %d, weekend email: %d, total: %d' % (weekday_count, weekend_count, total))

wdp = weekday_count / total * 100
wep = weekend_count / total * 100

print('weekday percentage: %.2f, weekend percentage: %.2f' % (wdp, wep))