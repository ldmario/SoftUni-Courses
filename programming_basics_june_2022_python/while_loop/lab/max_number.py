import sys

max_number = -sys.maxsize
current_number = -sys.maxsize

while current_number != "Stop":
    current_number = int(current_number)
    if int(current_number) > max_number:
        max_number = current_number
    current_number = input()

print(max_number)
