import sys

min_number = sys.maxsize
current_number = sys.maxsize

while current_number != "Stop":
    current_number = int(current_number)
    if current_number < min_number:
        min_number = current_number
    current_number = input()

print(min_number)
