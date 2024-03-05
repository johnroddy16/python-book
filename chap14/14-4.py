# the simple floor conversion program that demonstrates a comlpete program that takes some imput, does some processing and 
# produces some output:

usf = input('enter united states floor number: ')
try:
    i = int(usf)
except:
    print('you must enter a number for this program to work, %s is unacceptable' % usf)
    exit()
non_usf = i - 1
print('the non united states floor number is %d, have a nice day' % non_usf)