nylon = int(input())
paint = int(input())
liters = int(input())
hours = int(input())
nylon1 = 1.50
paint1 = 14.50
liters1 = 5
nylon_price = (nylon + 2) * nylon1
paint_price = (paint + 0.1 * paint) * paint1
liters_price = liters * liters1
bag_price = 0.40
full_price = nylon_price + paint_price + liters_price + bag_price
price_workers = (full_price * 0.30) * hours
final_price = full_price + price_workers
print(final_price)
