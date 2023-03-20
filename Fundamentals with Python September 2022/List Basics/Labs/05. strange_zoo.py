head = input()
body = input()
tail = input()

animal = [head, body, tail]

animal[0], animal[2] = animal[2], animal[0]

print(animal)

"""
                                            PROBLEM DESCRIPTION ! 


      STRANGE ZOO:
      
      You are at the zoo, and the meerkats look strange. 
      You will receive 3 strings on separate lines, representing the tail, the body,
      and the head of an animal in that order. Your task is to re-arrange the elements in a list
      so that the animal looks normal again:
      
      On the first position is the head;
      On the second position is the body;
      On the last one is the tail.
       
       Example input 1:           Output 1:         

        T                         [H, B, T]       
        B                                         
        H

"""
