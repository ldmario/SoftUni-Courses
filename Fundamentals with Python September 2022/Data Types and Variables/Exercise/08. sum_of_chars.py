number_of_lines = int(input())
sum_of_letters = 0

for _ in range(number_of_lines):
    letter = ord(input())
    sum_of_letters += letter

print(f"The sum equals: {sum_of_letters}")
