from math import ceil
name = input()
episode = int(input())
lunch_break = int(input())
time_lunch = lunch_break * 1/8
time_rest = lunch_break * 1/4
left = lunch_break - time_lunch - time_rest
diff = ceil(abs(episode - left))
if left >= episode:
    print(f"You have enough time to watch {name} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {diff} more minutes.")
