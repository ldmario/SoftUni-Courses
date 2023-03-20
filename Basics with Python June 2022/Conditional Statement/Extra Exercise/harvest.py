from math import floor, ceil


x = int(input())    # square meters vineyard
y = float(input())  # grape for 1 square meter
z = int(input())    # needed liters vine for sale
workers = int(input())  # number of workers
kilograms_grape = x * y
grape_for_vine = kilograms_grape * 40 / 100
liters_vine = grape_for_vine / 2.5

if liters_vine >= z:
    print(f"Good harvest this year! Total wine: {ceil(liters_vine)} liters.")
    liters_left = liters_vine - z
    liters_per_worker = liters_left / workers
    print(f"{ceil(liters_left)} liters left -> {ceil(liters_per_worker)} liters per person.")
else:
    more_vine = abs(liters_vine - z)
    print(f"It will be a tough winter! More {floor(more_vine)} liters wine needed.")
