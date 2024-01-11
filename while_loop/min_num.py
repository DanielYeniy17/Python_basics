import sys
min_num = sys.maxsize
while True:
    num = input()
    if num == 'Stop':
        break

    if min_num >= int(num):
        min_num = int(num)
print(min_num)
