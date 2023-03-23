from math import floor

ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
average_height_astronauts = float(input())

rocket_volume = ship_height * ship_length * ship_width
room_volume = (average_height_astronauts + 0.40) * 2 * 2
rocket_capacity = rocket_volume / room_volume

if 3 <= floor(rocket_capacity) <= 10:
    print(f"The spacecraft holds {floor(rocket_capacity)} astronauts.")
elif floor(rocket_capacity) < 3:
    print("The spacecraft is too small.")
elif 10 < floor(rocket_capacity):
    print("The spacecraft is too big.")
