type_flowers = input()
quantity = int(input())
budget = int(input())
total_sum = 0

if type_flowers == "Roses":
    if quantity > 80:
        total_sum = quantity * 5.00 * 0.90
    else:
        total_sum = quantity * 5.00
elif type_flowers == "Dahlias":
    if quantity > 90:
        total_sum = quantity * 3.80 * 0.85
    else:
        total_sum = quantity * 3.80
elif type_flowers == "Tulips":
    if quantity > 80:
        total_sum = quantity * 2.80 * 0.85
    else:
        total_sum = quantity * 2.80
elif type_flowers == "Narcissus":
    if quantity < 120:
        total_sum = quantity * 3 * 1.15
    else:
        total_sum = quantity * 3
elif type_flowers == "Gladiolus":
    if quantity < 80:
        total_sum = quantity * 2.50 * 1.20
    else:
        total_sum = quantity * 2.50

money_left = abs(budget - total_sum)

if budget >= total_sum:
    print(f"Hey, you have a great garden with {quantity} {type_flowers} and {money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_left:.2f} leva more.")
