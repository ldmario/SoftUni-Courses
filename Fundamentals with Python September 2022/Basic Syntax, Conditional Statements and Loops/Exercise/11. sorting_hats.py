name = input()
house = ""
while name != "Welcome!":

    if name == "Voldemort":
        print("You must not speak of that name!")
        break

    chars_in_name = len(name)

    if chars_in_name < 5:
        house = "Gryffindor"
    elif chars_in_name == 5:
        house = "Slytherin"
    elif chars_in_name == 6:
        house = "Ravenclaw"
    elif chars_in_name > 6:
        house = "Hufflepuff"

    print(f"{name} goes to {house}.")

    name = input()

else:
    print("Welcome to Hogwarts.")
