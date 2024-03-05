# just playing with split and join:

words = 'this is the way'

word_list = words.split()
print(word_list)

d = '-_-_'
x = d.join(word_list)
print(x)

z = 4.886678

y = float('%.2f' % z)  # will be a string without float() function 

print(y, type(y))