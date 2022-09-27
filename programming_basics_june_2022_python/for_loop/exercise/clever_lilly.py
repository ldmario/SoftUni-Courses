age = int(input())
laundry = float(input())
toy_price = int(input())

toys = 0
saved_money = 0

for years in range(1, age + 1):
    if years % 2 == 0:
        saved_money += years * 10 / 2
        saved_money -= 1.00
    else:
        toys += 1

money_from_toys = toys * toy_price
saved_money += money_from_toys
difference = abs(saved_money - laundry)

if saved_money >= laundry:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
