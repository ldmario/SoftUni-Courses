from math import ceil

name = input()
episode_duration = int(input())
break_duration = int(input())

time_for_lunch = break_duration / 8
time_for_rest = break_duration / 4
time_left_for_serial = break_duration - time_for_rest - time_for_lunch
total_time_left = abs(time_left_for_serial - episode_duration)

if time_left_for_serial >= episode_duration:
    print(f"You have enough time to watch {name} and left with {ceil(total_time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {ceil(total_time_left)} more minutes.")