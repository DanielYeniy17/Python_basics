pen = 5.80
marker = 7.20
preparation = 1.20
pen_count = int(input())
marker_count = int(input())
liters = int(input())
percentage = int(input()) / 100
pen_price = pen * pen_count
marker_price = marker_count * marker
preparation_price = preparation * liters
price = pen_price + marker_price + preparation_price
percentage_discount = price * percentage
final_price = price - percentage_discount
print(final_price)
