# writing the guardian statement in one line:

fhand = open('mbox-short.txt')

for a in fhand:
    a = a.split()  
    # if len(a) < 1: continue  
    # if len(a) < 3: continue 
    # if a[0] != 'From': continue
    # write the guardian pattern in one line:
    if len(a) < 3 or a[0] != 'From': continue  # very nice!
    print(a[2])  

fhand.close()