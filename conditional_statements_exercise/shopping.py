budged = float(input())
count_vcard = int(input())
count_proc = int(input())
count_ram = int(input())
price_vcard = 250 * count_vcard
price_proc1 = 0.35 * price_vcard
price_proc = count_proc * price_proc1
price_ram1 = 0.1 * price_vcard
price_ram = count_ram * price_ram1
price = price_ram + price_proc + price_vcard
discount = price - (0.15 * price)
if count_vcard > count_proc:
    price *= 0.85
diff = abs(budged - price)

if budged >= price:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')
