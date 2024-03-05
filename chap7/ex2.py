# exercise 2 from p4e chapter 7:

# read thru a file and pull out the lines that start with X-DSPAM-Confidence: :

print()

def dspam():
    name = input('enter a file name: ')
    print()
    if name == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - you have been punk\'d')
        exit()
    try:
        fhand = open(name)
    except:
        print('file not found: %s, exiting program now' % name)
        exit()
    
    lines = 0

    spam_sum = 0

    for a in fhand:
        a = a.rstrip()
        if not a.startswith('X-DSPAM-Confidence:'): continue
        b = a.find(' ')
        c = a[b+1:]
        d = float(c)
        spam_sum += d
        lines += 1
    
    avg = spam_sum / lines

    print('%.12f' % avg)

    print()

    fhand.close()

dspam()