budget = float(input())
season = input()
sleeping_cost = 0
destination = ""    # Bulgaria, Balkans, Europe
kind_of_stay = ""   # Camp or Hotel
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        kind_of_stay = "Camp"
        sleeping_cost = budget * 0.70
    elif season == "winter":
        kind_of_stay = "Hotel"
        sleeping_cost = budget * 0.30
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == "summer":
        kind_of_stay = "Camp"
        sleeping_cost = budget * 0.60
    elif season == "winter":
        kind_of_stay = "Hotel"
        sleeping_cost = budget * 0.20
elif budget > 1000:
    destination = "Europe"
    if season == "summer" or season == "winter":
        kind_of_stay = "Hotel"
        sleeping_cost = budget * 0.10
money_spent = budget - sleeping_cost
print(f"Somewhere in {destination}")
print(f"{kind_of_stay} - {money_spent:.2f}")
