import sys

num = int(input())

max_num = -sys.maxsize
min_num = sys.maxsize

for i in range(num):
    current = int(input())

    if current > max_num:
        max_num = current

    if current < min_num:
        min_num = current

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')
