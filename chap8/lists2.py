# trying to combine 2 lists in a certain way:

names = ['michael', 'john', 'kevin']

scores = [8, 7, 9]

for i in range(len(names)):  # for i in [0, 1, 2]:
    if i == 0:
        names.insert(i + 1, scores[i])  # names.insert(1, 8)
    else:
        names.insert(i + 2, scores[i])


print(names)