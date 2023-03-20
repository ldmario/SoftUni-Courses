movie_budget = float(input())
number_of_statists = int(input())
price_for_cloths = float(input())
decor = movie_budget * 0.10

if number_of_statists > 150:
    price_for_cloths *= 0.90

total_sum = price_for_cloths * number_of_statists + decor
money_left = abs(movie_budget - total_sum)

if movie_budget >= total_sum:
    print(f'''Action!
Wingard starts filming with {money_left:.2f} leva left.''')
else:
    print(f'''Not enough money!
Wingard needs {money_left:.2f} leva more.''')
