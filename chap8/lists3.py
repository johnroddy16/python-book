# seeing what happens when i run this program:

t = [4, 6, 8]

t = t.append(9)  # will not cause an error but will leave t with a return value of None

# t.append([4, 6])  # this is fine but will append a seperate list to the existing list

print(t)  # rinning all 4 lines will cause an error