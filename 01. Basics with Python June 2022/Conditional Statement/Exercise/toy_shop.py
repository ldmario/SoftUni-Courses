price_for_tour = float(input())
amount_puzzles = int(input())
amount_talking_dolls = int(input())
amount_teddy_bears = int(input())
amount_minions = int(input())
amount_trucks = int(input())
price_for_puzzles = amount_puzzles * 2.60
price_for_dolls = amount_talking_dolls * 3
price_for_teddy_bear = amount_teddy_bears * 4.10
price_for_minions = amount_minions * 8.20
price_for_trucks = amount_trucks * 2
total_amount = amount_puzzles + amount_talking_dolls + amount_teddy_bears + amount_minions + amount_trucks
total_price = price_for_puzzles + price_for_dolls + price_for_teddy_bear + price_for_minions + price_for_trucks

if total_amount >= 50:
    total_price = total_price - total_price * 25 / 100

money_after_rent = total_price - total_price * 10 / 100
money_left_need = abs(money_after_rent - price_for_tour)

if money_after_rent >= price_for_tour:
    print(f"Yes! {money_left_need:.2f} lv left.")
else:
    print(f"Not enough money! {money_left_need:.2f} lv needed.")
