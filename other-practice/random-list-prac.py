# random list practice:

import random

nums = [4, 8, 16, 32, 64, 128, 256, 512]

# print(nums[1:4])  # 1, 2, 3

x = random.randint(0, 7)
y = random.randint(1, 7)
# print(nums[1:1])

r = random.randint(0, 6)

if r == 4:
    y = None
elif x > y:
    x, y = y, x
elif x == y and y != 7:
    y += 1
elif x == y and y == 7:
    x -= 1

z = nums[x:y]

print(z)
print()

print(f'{x}:{y}')