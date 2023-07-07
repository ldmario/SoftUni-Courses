array = list(map(int, input().split(' ')))


def reverse(array):
    if len(array) != 0:
        rev = array.pop(0)
        reverse(array)
        array.append(rev)
    return ' '.join([str(x) for x in array])


print(reverse(array))

#
#
# def reverse(numbers, reversed_numbers):
#     if len(numbers) == 0:
#         return
#     reversed_numbers.append(numbers.pop())
#     reverse(numbers, reversed_numbers)
#     return ' '.join([str(x) for x in reversed_numbers])
#
#
# print(reverse(array, []))
