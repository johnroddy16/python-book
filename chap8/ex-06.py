# taking numbers from a user as input and displaying the min and max numbers:

nums = []

while True:
    num = input('enter a number or type done to quit: ')
    if num.lower() == 'done': break
    try:
        x = float(num)
    except:
        print('please enter a number')
        continue
    nums.append(x)


y = max(nums)

z = min(nums)

print()
print('maximum: %.1f' % y)
print()
print('minimum: %.1f' % z)
print()
print(float('09'))
print()