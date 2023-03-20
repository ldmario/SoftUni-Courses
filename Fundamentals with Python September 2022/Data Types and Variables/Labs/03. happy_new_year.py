number = int(input()) + 1

while True:

    string_of_number = str(number)
    set_of_number = set(string_of_number)

    if len(string_of_number) == len(set_of_number):
        print(number)
        break
    else:
        number += 1
