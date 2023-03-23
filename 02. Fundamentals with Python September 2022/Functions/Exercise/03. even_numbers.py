# def even_numbers(a):
#     b = " ".join(a)
#     list_of_even = []
#     for number in b:
#         if number.isdigit():
#             if int(number) % 2 == 0:
#                 list_of_even.append(int(number))
#
#     return list_of_even
#
#
# number_input = input()
#
# filtered_numbers = even_numbers(number_input)
# print(filtered_numbers)

numbers = input().split()


def even_numbers(a):
    if int(a) % 2 == 0:
        return True
    return False


even_numbers_iterator = filter(even_numbers, numbers)
list_of_even_numbers = list(map(int, even_numbers_iterator))
print(list_of_even_numbers)
