# extract the hour from the From lines and display the most commone hours:

fhand = open('mbox.txt')

hours = {}

for a in fhand:
    a = a.split()
    if len(a) < 6 or a[0] != 'From': continue
    t = a[5]
    x = t.split(':')
    r = x[0]  # could say r = int(x[0]) but no need, the sort by the string version will be fine
    hours[r] = hours.get(r, 0) + 1

y = sorted([(a, b) for a, b in hours.items()])

for a, b in y:
    print(a, b)