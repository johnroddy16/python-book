# aliasing:

# if a refers to an object and you assign b = a, then both variables will refer to the same object:
# two references to the same object:

# we say that the object is aliased if there is more than one reference, meaning it has more than one name:

a = [2, 4, 6, 8]
b = a

print(b)
print(a is b)

b[1] = 6  # this will also change a
print(a)

nums = [1, 2, 3, 5]
nums_copy = nums[:]  # this will make a copy that will not change if the other references are changed
numbers = nums
numbers[1] = 4
print()
print(nums)
print(nums_copy)