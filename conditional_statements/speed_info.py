num = float(input())
if num <= 10:
    print('slow')
elif 10 < num <= 50:
    print('average')
elif 50 < num <= 150:
    print('fast')
elif 150 < num <= 1000:
    print('ultra fast')
else:
    print('extremely fast')
