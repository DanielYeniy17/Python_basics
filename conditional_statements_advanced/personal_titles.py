age = float(input())
title = input()

if age >= 16 and title == 'm':
    print('Mr.')
elif age < 16 and title == 'm':
    print('Master')
elif age >= 16 and title == 'f':
    print('Ms.')
elif age < 16 and title == 'f':
    print('Miss')
