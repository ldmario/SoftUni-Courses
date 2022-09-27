number_of_strings = int(input())

for _ in range(number_of_strings):
    current_string = input()
    if "," not in current_string and "." not in current_string and "_" not in current_string:
        print(f"{current_string} is pure.")
    else:
        print(f"{current_string} is not pure!")
