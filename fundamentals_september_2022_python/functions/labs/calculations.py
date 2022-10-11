operator = input()
first_num = int(input())
second_num = int(input())


def calculate(num1, num2, action):
    if action == "multiply":
        return num1 * num2
    elif action == "divide":
        return int(num1 / num2)
    elif action == "add":
        return num1 + num2
    elif action == "subtract":
        return num1 - num2


print(calculate(first_num, second_num, operator))
