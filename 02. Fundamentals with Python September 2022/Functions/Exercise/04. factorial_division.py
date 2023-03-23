def factorial_division(num1, num2):
    factorial_num1 = 1
    for num in range(1, num1 + 1):
        factorial_num1 *= num

    factorial_num2 = 1
    for num in range(1, num2 + 1):
        factorial_num2 *= num

    return factorial_num1 / factorial_num2


first_number = int(input())
second_number = int(input())
print(f"{factorial_division(first_number, second_number):.2f}")
