# read a file and print out the contents in uppercase:

print()

def upper_case():
    name = input('enter a file name: ')
    print()
    try:
        fhand = open(name)
    except:
        print('file not found: %s, exiting program now' % name)
        exit()
    
    for a in fhand:
        a = a.rstrip()
        print(a.upper())

    print()

    fhand.close()

upper_case()