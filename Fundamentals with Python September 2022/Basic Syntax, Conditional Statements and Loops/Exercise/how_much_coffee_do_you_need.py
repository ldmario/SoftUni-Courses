command = input()
number_of_coffee = 0

while command != "END":

    if command == "coding" or command == "CODING":
        if command.islower():
            number_of_coffee += 1
        elif command.isupper():
            number_of_coffee += 2

    elif command == "dog" or command == "cat" or command == "DOG" or command == "CAT":
        if command.islower():
            number_of_coffee += 1
        elif command.isupper():
            number_of_coffee += 2

    elif command == "movie" or command == "MOVIE":
        if command.islower():
            number_of_coffee += 1
        elif command.isupper():
            number_of_coffee += 2

    command = input()

if number_of_coffee > 5:
    print("You need extra sleep")
else:
    print(number_of_coffee)
