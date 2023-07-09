def get_fibonacci(number):
    if number <= 1:
        return 1
    else:
        return (get_fibonacci(number - 1) + get_fibonacci(number - 2))


number = int(input())

print(get_fibonacci(number))
