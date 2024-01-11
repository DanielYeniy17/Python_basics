annual_tax = int(input())
sneakers = annual_tax - (annual_tax * 0.40)
kit = sneakers - (sneakers * 0.20)
ball = kit / 4
accessories = ball / 5
price = sneakers + kit + ball + accessories + annual_tax
print(price)
