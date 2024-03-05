# more practice from p4e book:

names = list()  # [] would do here

while True:
    n = input('pick a name or hit enter to choose a delimeter: ')
    if len(n) < 1 and len(names) < 1: 
        print('no names entered, exiting program now')
        exit()
    if len(n) < 1:
        d = input('enter delimeter: ')
        break         
    names.append(n)

k = d.join(names)

print(k)