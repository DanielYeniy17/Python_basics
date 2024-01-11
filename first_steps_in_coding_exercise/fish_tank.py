length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume = length * width * height
liters = volume / 1000
space = percentage / 100
needed_liters = liters * (1 - space)
print(needed_liters)
