product = input()
city = input()
quantity = float(input())
price = 0

if city == 'Sofia':
    if product == 'coffee':
        price = 0.50 * quantity
        print(price)
    elif product == 'water':
        price = 0.80 * quantity
        print(price)
    elif product == 'beer':
        price = 1.20 * quantity
        print(price)
    elif product == 'sweets':
        price = 1.45 * quantity
        print(price)
    elif product == 'peanuts':
        price = 1.60 * quantity
        print(price)

if city == 'Plovdiv':
    if product == 'coffee':
        price = 0.40 * quantity
        print(price)
    elif product == 'water':
        price = 0.70 * quantity
        print(price)
    elif product == 'beer':
        price = 1.15 * quantity
        print(price)
    elif product == 'sweets':
        price = 1.30 * quantity
        print(price)
    elif product == 'peanuts':
        price = 1.50 * quantity
        print(price)

if city == 'Varna':
    if product == 'coffee':
        price = 0.45 * quantity
        print(price)
    elif product == 'water':
        price = 0.70 * quantity
        print(price)
    elif product == 'beer':
        price = 1.10 * quantity
        print(price)
    elif product == 'sweets':
        price = 1.35 * quantity
        print(price)
    elif product == 'peanuts':
        price = 1.55 * quantity
        print(price)
