string_of_numbers = input()

list_of_numbers = string_of_numbers.split(' ')
reversed_list_of_numbers = []

for index in range(len(list_of_numbers)):
    number = int(list_of_numbers[index]) * -1
    reversed_list_of_numbers.append(number)

print(reversed_list_of_numbers)

"""
                                            PROBLEM DESCRIPTION !


        INVERTED VALUES:

        Write a program that receives a single string containing positive and negative string_of_numbers
        separated by a single space.
        Print a list containing the opposite of each number.

                           Input 1	                  Output 1
                        1 2 -3 -3 5	             [-1, -2, 3, 3, -5]

                           Input 2                    Output 2
                      -4 0 2 57 -101	        [4, 0, -2, -57, 101]

"""
