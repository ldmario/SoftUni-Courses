# def get_fibonacci(number):
#     if number <= 1:
#         return 1
#     else:
#         return (get_fibonacci(number - 1) + get_fibonacci(number - 2))
#
#
# number = int(input())
#
# print(get_fibonacci(number))

def calculate_fibonacci(number):
    one_fib = 0
    second_fib = 1
    result = 0
    for fib in range(number):
        result = one_fib + second_fib
        one_fib, second_fib = second_fib, result

    return result


print(calculate_fibonacci(int(input())))
