# insertion sort in python:

nums = [8, 7, 5, 4, 9, 2]

# insertion sort is not great for large sets of data as it uses nested loops 

# O(n ** 2)

# a python function for insertion sort:

def insertion_sort(nums):
    for i in range(1, len(nums)):  # for i in [1, 2, 3, 4, 5]
        for j in range(i-1, 0, -1):  # for j in [0], [1, 0], [2, 1, 0], [3, 2, 1, 0], [4, 3, 2, 1, 0]
            if nums[j] > nums[j + 1]:  # if 7 > 8
                nums[j], nums[j + 1] = nums[j + 1], nums[j]  # swap places 
             
    return nums  

x = insertion_sort(nums)

print(x)

print()

y = list(range(10, 0, -1))
print(y)