loop_interation = int(input())
tank_capacity = 0

for _ in range(loop_interation):
    liters_of_water = int(input())

    if tank_capacity + liters_of_water <= 255:
        tank_capacity += liters_of_water
    else:
        print("Insufficient capacity!")

else:
    print(tank_capacity)
