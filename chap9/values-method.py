# search thru the values of a dict with the vlaues() method:

name_and_num = {
    'michael': 206_418_8234,
    'kevin': 9072284934,
    'carolyn': 2062954876,
    'mom': 2063567535,
    'juan': 2063802424,
}

nums = list(name_and_num.values())

print(nums)

# traverse nums:

numbers = [2064188234, 2062954876, 2063567535, 17]

for n in numbers:
    if n not in nums:
        print('no')
        continue
    print('yes, %d' % n)