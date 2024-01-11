a, b, c = int(input()), int(input()), int(input())
sum = a + b + c
minutes = sum // 60
seconds = sum % 60
if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
