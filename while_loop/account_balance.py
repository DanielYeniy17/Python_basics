total = 0
while True:
    money = input()

    if money == 'NoMoreMoney':
        break

    if float(money) < 0:
        print('Invalid operation!')
        break
    print(f'Increase: {float(money):.2f}')
    total += float(money)

print(f'Total: {total:.2f}')
