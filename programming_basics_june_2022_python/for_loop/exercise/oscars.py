name_actor = input()
points_from_academy = float(input())
quantity_evaluators = int(input())
result = points_from_academy

for points in range(1, quantity_evaluators + 1):
    if result > 1250.5:
        break
    else:
        name_evaluator = input()
        points_from_evaluator = float(input())
        result += ((len(name_evaluator) * points_from_evaluator) / 2)

needed_points = 1250.5 - result

if result > 1250.5:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {result:.1f}!")
else:
    print(f"Sorry, {name_actor} you need {needed_points:.1f} more!")
