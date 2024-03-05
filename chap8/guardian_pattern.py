# rewriting the mbox and mbox-short search program to guard against empty lines:

fhand = open('mbox-short.txt')

for a in fhand:
    a = a.split()  # here we are skipping strip or rstrip 
    # if len(a) < 1: continue  # here we use gaurdian pattern to guard against empty lists from blank lines
    if len(a) < 3: continue # this will ensure we don't get an error if there are less than elements 
    if a[0] != 'From': continue
    print(a[2])  # works pretty fast but we still need to guard against non-blank lines that may have less than 
                 # 3 elements 
fhand.close()