lenght_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percent = float(input())
# 1 litter = 1 decimeter3

capacity_of_aquarium_in_liters = lenght_in_cm * width_in_cm * height_in_cm / 1000
percentage_of_non_free_space = percent / 100
needed_liters = capacity_of_aquarium_in_liters * (1 - percentage_of_non_free_space)
print(needed_liters)
