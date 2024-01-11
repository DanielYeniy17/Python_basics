import sys
max_num = -sys.maxsize
while True:
    num = input()
    if num == 'Stop':
        break
    if max_num <= int(num):
        max_num = int(num)
print(max_num)
