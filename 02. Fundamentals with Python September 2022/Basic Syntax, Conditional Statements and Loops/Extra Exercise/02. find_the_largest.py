number = input()

extracted_digits = []

for i in range(len(number)):
    extracted_digits.append(number[i])

extracted_digits.sort(reverse=True)

for digit in extracted_digits:
    print(digit, end="")
