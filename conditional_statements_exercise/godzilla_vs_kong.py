budget = float(input())
count = int(input())
price_costume = float(input())
decoration = 0.10 * budget
if count > 150:
    price_costume -= price_costume * 0.10

costume = count * price_costume
total = decoration + costume
diff = abs(budget - total)

if total > budget:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
