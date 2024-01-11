square_meters = float(input())
one_square_meter = 7.61
discount_percentage = 0.18
price = square_meters * one_square_meter
discount = price * discount_percentage
final_price = price - discount
print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount} lv.')
