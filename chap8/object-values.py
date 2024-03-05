# objects and values:

a = 'banana'
b = 'banana'

print(a is b)  # will output True since a and b point to the same object
               # they are not two different objects with the same value, python only created one object 
               # they both point to it

# with two lists you get two objects:

x = [4, 6, 8]  # the two lists are equivalent but not identical because they are not the same object
y = [4, 6, 8]

print(x is y)  # will output False since python created two different objects that have the same value
# if two objects are identical we would also consider them to be equivalent 

# an object has a value