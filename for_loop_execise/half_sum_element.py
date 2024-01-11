import sys
num = int(input())
max_num = -sys.maxsize
sum = 0
for i in range(num):
    current = int(input())
    if current > max_num:
        max_num = current
    sum += current
if (sum - max_num) == max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    print(f'Diff = {abs((sum - max_num) - max_num)}')
