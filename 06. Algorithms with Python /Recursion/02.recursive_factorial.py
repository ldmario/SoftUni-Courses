def calc_factorial(num):
    if num == 0:
        return 1
    return num * calc_factorial(num - 1)


num = int(input())

print(calc_factorial(num))
