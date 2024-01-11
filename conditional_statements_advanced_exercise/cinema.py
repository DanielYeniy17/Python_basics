type = input()
rows = int(input())
columns = int(input())
space = rows * columns
income = 0
if type == 'Premiere':
    income = space * 12
elif type == 'Normal':
    income = space* 7.5
elif type == 'Discount':
    income = space * 5
print(f'{income:.2f} leva')