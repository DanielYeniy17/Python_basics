num = int(input())
even = 0
odd = 0
for i in range(1, num + 1):
    current = int(input())

    if i % 2 == 0:
        even += current
    else:
        odd += current
if even == odd:
    print('Yes')
    print(f'Sum = {even}')
else:
    diff = abs(even - odd)
    print('No')
    print(f'Diff = {diff}')
