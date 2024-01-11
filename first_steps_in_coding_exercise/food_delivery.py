chicken_menu = 10.35
fish_menu = 12.40
veg_menu = 8.15

chicken_count = int(input())
fish_count = int(input())
veg_count = int(input())


chicken_price = chicken_count * chicken_menu
fish_price = fish_count * fish_menu
veg_price = veg_count * veg_menu

whole_price = chicken_price + fish_price + veg_price
dessert = whole_price * 0.2
delivery = 2.5

full_price = whole_price + dessert + delivery
print(full_price)
