deposit = float(input())
deposit_deadline_months = int(input())
annual_interest_rate = float(input()) / 100
interest = deposit * annual_interest_rate
interest_rate_one_month = interest / 12
price = deposit + deposit_deadline_months * interest_rate_one_month
print(price)
