number_of_int = int(input())

list_of_positive = []
list_of_negative = []

for _ in range(number_of_int):
    current_int = int(input())

    if current_int <= 0:
        list_of_negative.append(current_int)
    else:
        list_of_positive.append(current_int)

sum_of_negative = sum(num for num in list_of_negative)

print(list_of_positive)
print(list_of_negative)
print(f"Count of positives: {len(list_of_positive)}")
print(f"Sum of negatives: {sum_of_negative}")

"""
                                            PROBLEM DESCRIPTION ! 


       LIST STATISTIC:

       On the first line, you will receive a number n. On the following n lines, you will receive integers.
       You should create and print two lists:
       One with all the positives (including 0) string_of_numbers
       One with all the negatives string_of_numbers
       Finally, print the following message: 
       
       Count of positives: {count_positives}
       Sum of negatives: {sum_of_negatives}"
       
        Example input 1:           Output 1:         

        5                         [10, 3, 2]       
        10                        [-15, -4]                  
        3                         Count of positives: 3
        2                         Sum of negatives: -19         
        -15                                         
        -4

"""
