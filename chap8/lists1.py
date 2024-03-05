# traversing a list:

nums = []


while True:
    contents = (input('what number should be added to the list? hit enter to end the program '))
    if len(contents) < 1:
        print('thank you for participating')
        break 
    try:
        x = int(contents)
    except:
        print('you must enter a number, %s will not do, please try again' % contents)
        continue

    nums.append(x)

for i in range(len(nums)):  # for i in [0, 1, 2, 3, ...] depending on the legth of the list
    nums[i] *= 2  # nums[i] will first be nums[0] unless the range starts at an index other than the 0th

print(nums)