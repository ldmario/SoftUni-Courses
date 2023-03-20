sequence_of_numbers = input().split()


def absolute():
    absolute_values = []
    for number in sequence_of_numbers:
        absolute_values.append(abs(float(number)))

    return absolute_values


absolute_result = absolute()
print(absolute_result)
