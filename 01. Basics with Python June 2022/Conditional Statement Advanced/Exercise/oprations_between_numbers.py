first_number = int(input())
second_number = int(input())
operator = input()
result = 0
if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if not second_number == 0:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result:.2f}")
    else:
        print(f"Cannot divide {first_number} by zero")
elif operator == "%":
    if not second_number == 0:
        result = first_number % second_number
        print(f"{first_number} % {second_number} = {result}")
    else:
        print(f"Cannot divide {first_number} by zero")
if result == first_number + second_number \
        or result == first_number - second_number \
        or result == first_number * second_number:
    if result % 2 == 0 and not operator == "/" and not operator == "%":
        print(f"{first_number} {operator} {second_number} = {result} - even")
    elif not result % 2 == 0:
        print(f"{first_number} {operator} {second_number} = {result} - odd")
