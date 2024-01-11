fruit = input()
day = input()
count = float(input())
banana = 0
apple = 0
orange = 0
grapefruit = 0
kiwi = 0
pineapple = 0
grapes = 0
condition = True

if day in 'Monday Tuesday Wednesday Thursday Friday':
    banana = 2.50
    apple = 1.20
    orange = 0.85
    grapefruit = 1.45
    kiwi = 2.70
    pineapple = 5.50
    grapes = 3.85
elif day in 'Saturday Sunday':
    banana = 2.70
    apple = 1.25
    orange = 0.90
    grapefruit = 1.60
    kiwi = 3.00
    pineapple = 5.60
    grapes = 4.20
else:
    condition = False
    print('error')

if condition:
    if fruit == 'banana':
        print(f'{banana * count:.2f}')
    elif fruit == 'apple':
        print(f'{apple * count:.2f}')
    elif fruit == 'orange':
        print(f'{orange * count:.2f}')
    elif fruit == 'grapefruit':
        print(f'{grapefruit * count:.2f}')
    elif fruit == 'kiwi':
        print(f'{kiwi * count:.2f}')
    elif fruit == 'pineapple':
        print(f'{pineapple * count:.2f}')
    elif fruit == 'grapes':
        print(f'{grapes * count:.2f}')
    else:
        print('error')
    condition = False
