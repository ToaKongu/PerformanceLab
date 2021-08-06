import sys


n = int(sys.argv[1])
m = int(sys.argv[2])
mass = [int(i) for i in range(1, n + 1)]
result = []
value_n = 0
value_m = 0
while True:
    value_m += 1
    value_n += 1
    if value_m == m:
        value_m = 0
        result.append(str(mass[value_n - n % m]) if value_n - m < -
                      len(mass) else str(mass[value_n - m]))
        if value_n == 1:
            break
        value_n -= 1
    if value_n == n:
        value_n = 0
print(''.join(result))
