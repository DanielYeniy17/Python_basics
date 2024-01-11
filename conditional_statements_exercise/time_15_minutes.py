hours = int(input())
minutes = int(input())
time = (hours * 60) + minutes + 15
current_minutes = time % 60
current_hours = time // 60

if current_hours > 23:
    print(f'0:{current_minutes:02d}')
else:
    print(f'{current_hours}:{current_minutes:02d}')
