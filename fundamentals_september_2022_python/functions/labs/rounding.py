input_numbers = input().split()


def rounding(given_list):
    rounded_list = []
    for num in given_list:
        rounded_list.append(round(float(num)))

    return rounded_list


new_list = rounding(input_numbers)
print(new_list)
