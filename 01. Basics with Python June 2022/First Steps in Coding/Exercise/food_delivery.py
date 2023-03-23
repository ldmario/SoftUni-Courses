amount_of_chicken_menu = int(input())
amount_of_fish_menu = int(input())
amount_of_vegetarian_menu = int(input())
price_for_chicken_menu = amount_of_chicken_menu * 10.35
price_for_fish_menu = amount_of_fish_menu * 12.40
price_for_vegetarian_menu = amount_of_vegetarian_menu * 8.15
total_price_for_order = price_for_vegetarian_menu + price_for_fish_menu + price_for_chicken_menu
desert_menu = total_price_for_order * 0.20
final_sum = total_price_for_order + desert_menu + 2.50
print(f"{final_sum:.2f}")
