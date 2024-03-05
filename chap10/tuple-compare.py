# comparing tuples:

x = 4, 8, 20, 10
y = 4, 8, 2, 100

print(x > y)  # True, x is greater than y because the algorithm stops at 20 > 2 and never gets to 10 < 100

f = 4, 8, 20, 10
g = 4, 8.4, 20 , 1

print(f > g)  # False, 8.4 > 8

h = 4, 'eight', 12, 20  # comparing h to i will throw an error at 'eight' and 8
i = 4, 8, 12, 20

j = 4, 'six', 12, 20
print(j > h)  # True, 'six' > 'eight'

k = 'Six', 7, 8, 9
l = 'four', 5, 6, 7

print(l > k)  # True, 'four', since lower case, > 'Six", even though f is less than s in alphabet, it does ascii