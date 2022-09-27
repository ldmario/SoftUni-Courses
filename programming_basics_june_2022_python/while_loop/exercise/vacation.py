needed_money = float(input())
current_money = float(input())
failed_saving = False
days = 0
spending_days = 0

while current_money < needed_money:
    if spending_days == 5:
        failed_saving = True
        break
    action = input()
    money_spend_or_saved = float(input())
    days += 1
    if action == "spend":
        spending_days += 1
        current_money -= money_spend_or_saved
        if current_money < 0:
            current_money = 0
    elif action == "save":
        current_money += money_spend_or_saved
        spending_days = 0

if failed_saving:
    print("You can't save the money.")
    print(f"{days}")
else:
    print(f"You saved the money for {days} days.")
