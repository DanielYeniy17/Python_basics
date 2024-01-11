num = int(input())
left = 0
right = 0
for i in range(num):
    current = int(input())
    left += current

for i in range(num):
    current = int(input())
    right += current

if left == right:
    print(f'Yes, sum = {left}')
else:
    print(f'No, diff = {abs(left - right)}')
