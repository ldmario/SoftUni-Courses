numbers_of_int = int(input())
integers = []
filtered_int = []

for _ in range(numbers_of_int + 1):
    current_int = input()

    if current_int == "even":
        for num in integers:
            if num % 2 == 0 or num == 0:
                filtered_int.append(num)
    elif current_int == "odd":
        for num in integers:
            if num % 2 != 0:
                filtered_int.append(num)
    elif current_int == "positive":
        for num in integers:
            if num >= 0:
                filtered_int.append(num)
    elif current_int == "negative":
        for num in integers:
            if num < 0:
                filtered_int.append(num)
    else:
        current_int = int(current_int)
        integers.append(current_int)

print(filtered_int)


"""
                                            PROBLEM DESCRIPTION ! 
                    

        NUMBER FILTER:

        On the first line, you will receive a single number n. On the following n lines, you will receive integers.
        After that, you will be given one of the following commands:
        even
        odd
        negative
        positive
        Filter all the string_of_numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

        Example input 1:           Output 1:          Example input 2:            Output 2:

        1                         [-2, 18, 998]       3                               [-4]
        5                                             111
        33                                            -4
        19                                            0
        -2                                            negative
        18
        998
        even
"""
