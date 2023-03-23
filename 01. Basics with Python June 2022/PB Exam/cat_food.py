amount_cats = int(input())
quantity_food_needed = 0
group_1 = 0
group_2 = 0
group_3 = 0

for _ in range(amount_cats):
    grams_food = float(input())

    if 100 <= grams_food < 200:
        group_1 += 1
        quantity_food_needed += grams_food
    elif 200 <= grams_food < 300:
        group_2 += 1
        quantity_food_needed += grams_food
    elif 300 <= grams_food < 400:
        group_3 += 1
        quantity_food_needed += grams_food

money_needed = (quantity_food_needed / 1000) * 12.45

print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day: {money_needed:.2f} lv.")
