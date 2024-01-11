time = int(input())
day = input()

if 10 <= time <= 18 and day != 'Sunday':
    print('open')
else:
    print('closed')
