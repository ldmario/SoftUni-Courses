number1 = int(input())
number2 = int(input())
number3 = int(input())
number4 = int(input())

changes_counter = 0
reached_limit_of_changes = False

for num1 in range(number1, 8 + 1):
    for num2 in range(9, number2 - 1, -1):
        for num3 in range(number3, 8 + 1):
            for num4 in range(9, number4 - 1, -1):
                if num1 % 2 == 0 and num2 % 2 != 0 and num3 % 2 == 0 and num4 % 2 != 0:
                    if num1 == num3 and num2 == num4:
                        print("Cannot change the same player.")
                    else:
                        changes_counter += 1
                        print(f"{num1}{num2} - {num3}{num4}")
                    if changes_counter == 6:
                        reached_limit_of_changes = True
                        break
            if reached_limit_of_changes:
                break
        if reached_limit_of_changes:
            break
    if reached_limit_of_changes:
        break
