string_of_numbers = input()
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
reversed_number = 0
reversed_numbers = []
for index, char in enumerate(string_of_numbers):
    if char in numbers:
        if index < len(string_of_numbers) - 2:
            if string_of_numbers[index + 1] in numbers:
                current_number = int(string_of_numbers[index + (index + 1)])
            else:
                current_number = int(char)
        else:
            current_number = int(char)
        if string_of_numbers[index - 1] == "-":
            current_number = -int(char)
        reversed_number = current_number * -1
        reversed_numbers.append(reversed_number)

print(reversed_numbers)

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
