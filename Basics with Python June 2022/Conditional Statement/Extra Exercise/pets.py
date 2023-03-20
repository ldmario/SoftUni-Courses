from math import floor, ceil

days = int(input())
kilograms_food = int(input())
dogs_food = float(input())  # in kilograms
cats_food = float(input())  # in kilograms
turtles_food = float(input())   # in grams
turtles_food_in_kg = turtles_food / 1000
total_food = (dogs_food  + cats_food + turtles_food_in_kg) * days
food_left = abs(kilograms_food - total_food)
if total_food <= kilograms_food:
    print(f"{floor(food_left)} kilos of food left.")
else:
    print(f"{ceil(food_left)} more kilos of food are needed.")