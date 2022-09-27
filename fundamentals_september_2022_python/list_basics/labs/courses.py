number_of_strings = int(input())

created_list = []

for _ in range(number_of_strings):
    current_str = input()

    created_list.append(current_str)

print(created_list)

"""
                                            PROBLEM DESCRIPTION ! 


    COURSES:
    
    On the first line, you will receive a single number n.
    On the following n lines, you will receive names of courses. 
    You should create a list of courses and print it.

       Example input 1:                        Output 1:         

        PB Python                        ['PB Python', 'PF Python']       
        PF Python                                       

"""
