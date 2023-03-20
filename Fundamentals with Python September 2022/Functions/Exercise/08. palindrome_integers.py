def palindrome_integers(integer_number):
    for num in integer_number:
        if num == num[::-1]:
            print("True")
        else:
            print("False")


number = input().split(", ")
palindrome_integers(number)
