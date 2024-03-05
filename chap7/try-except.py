# introducing try and except to the file play:

print()

def subject_line():
    name = input('enter a file name: ')
    print()
    try:
        fhand = open(name)
    except:
        print('file not found: %s, exiting program now' % name)
        exit()
    
    kount = 0

    for a in fhand:
        a = a.rstrip()
        if not a.startswith('Subject:'): continue
        print(a[:20])
        kount += 1
    
    print()

    print('there were %d subject lines in the file %s' % (kount, name))
    
    fhand.close()

subject_line() 

print()