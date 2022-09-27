from math import floor, ceil

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactus = int(input())
gift_cost = float(input())
total_sum = magnolias * 3.25 +\
            hyacinths * 4 +\
            roses * 3.5 +\
            cactus * 8
total_sum *= 0.95
money_left = abs(total_sum - gift_cost)
if gift_cost <= total_sum:
    print(f"She is left with {floor(money_left)} leva.")
else:
    print(f"She will have to borrow {ceil(money_left)} leva.")
