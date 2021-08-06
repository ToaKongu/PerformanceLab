import sys


file = open(f'{sys.argv[1]}', 'r')
nums = file.read()
file.close()
nums = nums.split()

summa = 0
for i in nums:
    summa += int(i)
x = summa // len(nums)
result = 0
for i in nums:
    result += abs(int(i) - x)
print(result)
