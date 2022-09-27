n = int(input())
odd_number = False
last_num = 0

for _ in range(n):
    num = int(input())
    if num % 2 == 1:
        odd_number = True
        last_num = num
        break

if odd_number:
    print(f"{last_num} is odd!")
else:
    print("All string_of_numbers are even.")
