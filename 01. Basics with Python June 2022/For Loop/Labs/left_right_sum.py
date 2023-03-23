loops = int(input())

sum_first_two = 0
sum_second_two = 0

for _ in range(1, loops + 1):
    current_number = int(input())
    sum_first_two += current_number

for _ in range(1, loops + 1):
    current_number = int(input())
    sum_second_two += current_number

diff = abs(sum_first_two - sum_second_two)

if sum_first_two == sum_second_two:
    print(f"Yes, sum = {sum_first_two}")
elif sum_first_two != sum_second_two:
    print(f"No, diff = {diff}")
