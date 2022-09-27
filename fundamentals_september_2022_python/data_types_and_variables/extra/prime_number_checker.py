number = int(input())
number_is_prime = True

for num in range(2, number):
    if number % num == 0:
        number_is_prime = False
        break

print(number_is_prime)

# if number_is_prime:
#     print(number_is_prime)
# elif not number_is_prime:
#     print(number_is_prime)
