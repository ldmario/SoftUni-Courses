budget = float(input())
category = input()
people = int(input())
budget_after_transport = 0
money_left = 0
tickets = 0

if 0 < people <= 4:
    budget_after_transport = budget * 0.25
elif 5 <= people <= 9:
    budget_after_transport = budget * 0.40
elif 10 <= people <= 24:
    budget_after_transport = budget * 0.50
elif 25 <= people <= 49:
    budget_after_transport = budget * 0.60
elif people >= 50:
    budget_after_transport = budget * 0.75

if category == "VIP":
    tickets = 499.99 * people
    money_left = budget_after_transport - tickets
    if 0 > money_left:
        print(f"Not enough money! You need {abs(money_left):.2f} leva.")
    elif 0 <= money_left:
        print(f"Yes! You have {money_left:.2f} leva left.")
elif category == "Normal":
    tickets = 249.99 * people
    money_left = budget_after_transport - tickets
    if 0 > money_left:
        print(f"Not enough money! You need {abs(money_left):.2f} leva.")
    elif 0 <= money_left:
        print(f"Yes! You have {money_left:.2f} leva left.")
