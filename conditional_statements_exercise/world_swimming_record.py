sec = float(input())
met = float(input())
met_sec = float(input())
sec1 = met * met_sec
num1 = int(met / 15)
num2 = num1 * 12.5
time = sec1 + num2

if time < sec:
    print(f'Yes, he succeeded! The new world record is{time: .2f} seconds.')
if time >= sec:
    num3 = time - sec
    print(f'No, he failed! He was{num3: .2f} seconds slower.')
