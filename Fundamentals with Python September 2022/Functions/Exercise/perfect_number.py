def is_num_perfect(number):
    divisors = []
    for num in range(1, number + 1):
        if number % num == 0:
            divisors.append(num)
    sum_of_divisors = 0
    for num in divisors:
        sum_of_divisors += int(num)

    if sum_of_divisors / 2 == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


current_number = int(input())
is_num_perfect(current_number)
