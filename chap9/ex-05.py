fhand = open('mbox-short.txt')

school_count = {}

for a in fhand:
    a = a.split()
    if len(a) < 2 or a[0] != 'From': continue
    b = a[1]
    c = b.split('@')
    d = c[1]
    school_count[d] = school_count.get(d, 0) + 1


print(school_count)

x = max(list(school_count.values()))
print(x)

for a in school_count:
    if school_count[a] == x:
        print(a, school_count[a])