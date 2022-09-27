budget_of_group = int(input())
season = input().lower()
amount_fishers = int(input())
boat_price = 0
if season == "spring":
    if amount_fishers <= 6:
        boat_price = 3000 * 0.90
    elif 7 < amount_fishers <= 11:
        boat_price = 3000 * 0.85
    elif amount_fishers >= 12:
        boat_price = 3000 * 0.75
elif season == "winter":
    if amount_fishers <= 6:
        boat_price = 2600 * 0.90
    elif 7 < amount_fishers <= 11:
        boat_price = 2600 * 0.85
    elif amount_fishers >= 12:
        boat_price = 2600 * 0.75
elif season == "autumn" or season == "summer":
    if amount_fishers <= 6:
        boat_price = 4200 * 0.90
    elif 7 < amount_fishers <= 11:
        boat_price = 4200 * 0.85
    elif amount_fishers >= 12:
        boat_price = 4200 * 0.75
if amount_fishers % 2 == 0 and not season == "autumn":
    boat_price *= 0.95
money_left = abs(budget_of_group - boat_price)
if budget_of_group >= boat_price:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_left:.2f} leva.")
