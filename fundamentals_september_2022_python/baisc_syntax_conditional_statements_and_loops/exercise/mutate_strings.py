first_string = input()
second_string = input()
last_printed_string = first_string

for character_index in range(1, len(first_string) - 1):

    left_part = second_string[:character_index]
    right_part = first_string[character_index:]
    current_string = left_part + right_part

    if current_string == last_printed_string:
        continue

    print(current_string)

    last_printed_string = current_string
