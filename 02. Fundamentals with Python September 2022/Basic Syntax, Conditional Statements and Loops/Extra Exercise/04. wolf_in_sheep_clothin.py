animals = input()
current_animal = ""
list_of_animals = []

for char in animals:
    if char in "sheep" or char in "wolf":
        current_animal += char

    if current_animal == "sheep" or current_animal == "wolf":
        list_of_animals.append(current_animal)
        current_animal = ""

for index, animal in enumerate(list_of_animals):
    if animal == "wolf":
        if index < len(list_of_animals) - 1:
            sheep_position = len(list_of_animals) - (index + 1)
            print(f"Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!")
            break
        else:
            print("Please go away and stop eating my sheep")
            break
