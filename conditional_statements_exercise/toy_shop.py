price_trip = float(input())
puzzle = int(input())
doll = int(input())
bear = int(input())
minion = int(input())
trucks = int(input())

sum = (puzzle * 2.60) + (doll * 3) + (bear * 4.10) + (minion * 8.20) + (trucks * 2)
number_toys = puzzle + doll + bear + minion + trucks

if number_toys >= 50:
    sum -= sum * 0.25

rent = sum * 0.10
profit = sum - rent

diff = abs(profit - price_trip)
if profit >= price_trip:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')
