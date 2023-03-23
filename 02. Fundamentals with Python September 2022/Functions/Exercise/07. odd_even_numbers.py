def sum_odd_even(a):
    sum_odd = 0
    sum_even = 0
    for number in a:
        if number.isdigit():
            if int(number) % 2 == 0:
                sum_even += int(number)
            else:
                sum_odd += int(number)

    result = f"Odd sum = {sum_odd}, Even sum = {sum_even}"

    return result


string_of_numbers = input()

print(sum_odd_even(string_of_numbers))
