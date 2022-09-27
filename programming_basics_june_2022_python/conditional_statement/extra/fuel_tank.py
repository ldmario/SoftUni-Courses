type_fuel = input()
liters = float(input())
if type_fuel.lower() == "diesel" and liters >= 25:
    print(f"You have enough {type_fuel.lower()}.")
else:
    if type_fuel.lower() == "diesel" and liters < 25:
        print(f"Fill your tank with {type_fuel.lower()}!")
    else:
        if type_fuel.lower() == "gasoline" and liters >= 25:
            print(f"You have enough {type_fuel.lower()}.")
        else:
            if type_fuel.lower() == "gasoline" and liters < 25:
                print(f"Fill your tank with {type_fuel.lower()}!")
            else:
                if type_fuel.lower() == "gas" and liters >= 25:
                    print(f"You have enough {type_fuel.lower()}.")
                else:
                    if type_fuel.lower() == "gas" and liters < 25:
                        print(f"Fill your tank with {type_fuel.lower()}!")
                    else:
                        print("Invalid fuel!")
