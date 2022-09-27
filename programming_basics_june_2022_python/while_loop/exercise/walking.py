steps_per_day = 10000
steps_reached_daily = 0

while True:
    steps = input()
    if not steps == "Going home":
        steps = int(steps)
        steps_reached_daily += steps
        if steps_reached_daily >= steps_per_day:
            break
    else:
        steps_to_home = int(input())
        steps_reached_daily += steps_to_home
        break

diff = abs(steps_reached_daily - steps_per_day)

if steps_reached_daily >= steps_per_day:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
