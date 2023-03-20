number_of_messages = int(input())
print_message = ""
for _ in range(number_of_messages):
    current_number = int(input())

    if current_number == 88:
        print_message = "Hello"
    elif current_number == 86:
        print_message = "How are you?"
    elif current_number < 88:
        print_message = "GREAT!"
    else:
        print_message = "Bye."

    print(print_message)
