command = input()
sum_of_prime_numbers = 0
sum_of_non_prime_numbers = 0
number_is_non_prime = False
while not command == "stop":
    current_number = int(command)
    if current_number < 0:
        print("Number is negative.")
        command = input()
        continue

    for number in range(2, current_number):
        if current_number % number == 0:
            number_is_non_prime = True
            break

    if number_is_non_prime:
        sum_of_non_prime_numbers += current_number
    else:
        sum_of_prime_numbers += current_number
    number_is_non_prime = False
    command = input()

print(f"Sum of all prime numbers is: {sum_of_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_of_non_prime_numbers}")
