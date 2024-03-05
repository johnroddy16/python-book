# examlples of how to write a min max loop and other stuff:

total = 0

nums = [66, 44, 101, 106, 88, 99]

for num in nums:
    total += num

print(total)

largest = None

print('before:', largest)

for a in nums:
    if largest == None or a > largest:
        largest = a
    print(a, largest)

print('after:', largest)