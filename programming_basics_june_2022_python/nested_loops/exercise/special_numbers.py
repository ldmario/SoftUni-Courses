num = int(input())

for special_number in range(1111, 10000):
    special_number = str(special_number)
    valid_special_number = True

    for index, each_num_in_special_number in enumerate(special_number):
        each_num_in_special_number = int(each_num_in_special_number)

        if each_num_in_special_number == 0:
            valid_special_number = False
            continue

        if num % each_num_in_special_number != 0:
            valid_special_number = False
            break

    if valid_special_number:
        print(special_number, end=" ")
