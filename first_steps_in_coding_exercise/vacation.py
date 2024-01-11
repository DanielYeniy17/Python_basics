from math import floor
pages = int(input())
pages_per_hour = int(input())
days = int(input())
hours = floor(pages / pages_per_hour)
hours_per_day = hours / days
print(int(hours_per_day))
