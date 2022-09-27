number_of_floors = int(input())
number_of_flats = int(input())

for floor in range(number_of_floors, 0, -1):
    for flats in range(number_of_flats):
        if floor == number_of_floors:
            print(f"L{floor}{flats}", end=" ")
        elif floor % 2 == 0:
            print(f"O{floor}{flats}", end=" ")
        else:
            print(f"A{floor}{flats}", end=" ")
    print()
