amount_of_string = int(input())
keyword = input()

list_of_str = []
list_of_str_with_word = []

for _ in range(amount_of_string):
    current_str = input()
    if keyword in current_str:
        list_of_str_with_word.append(current_str)

    list_of_str.append(current_str)

print(list_of_str)
print(list_of_str_with_word)

"""
                                            PROBLEM DESCRIPTION ! 


        SEARCH:

        On the first line, you will receive a number n. On the second line, you will receive a word.
        On the following n lines, you will be given some strings. You should add them to a list and print them.
        After that, you should filter out only the strings that include the given word and print that list too.
        
        Example input 1:                                         Output 1:      
                                               ["I study at SoftUni", "I walk to work", "I learn Python at SoftUni"]
        3                                      ["I study at SoftUni", "I learn Python at SoftUni"]      
        SoftUni                                       
        I study SoftUni                                     
        I walk to work                                           
        I learn Python at SoftUni                                           

"""
