# object-oriented programming:

# simple example of oop in action:

stuff = list()  # contstruct an object of type list
stuff.append('python')  # calls the append method
stuff.append('chuck')
stuff.sort()  # calls the sort method
print(stuff[0])  # retrieves the item at position 0
print(stuff.__getitem__(0))  # calls get_item method on stuff with a parameter of 0
print(list.__getitem__(stuff, 0))  # calls get_item method in the list class and passes the list and item as parameters


# look at the capabilities of an object with the dir() function:

print(dir(stuff))
print()
print(dir(list()))