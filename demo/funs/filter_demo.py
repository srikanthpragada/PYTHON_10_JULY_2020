def iseven(n):
    return n % 2 == 0


nums = [10, 11, 99, 87, 76, 373]

for n in filter(iseven, nums):
    print(n)

for n in filter(lambda n: n % 2 == 1, nums):
    print(n)
