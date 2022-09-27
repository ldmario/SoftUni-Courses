numbers_of_pens = int(input())
numbers_of_markers = int(input())
liters_of_detergent = int(input())
percentage_of_discount = int(input())
price_of_pens = numbers_of_pens * 5.80
price_of_markers = numbers_of_markers * 7.20
price_of_detergent = liters_of_detergent * 1.20
discount = percentage_of_discount / 100
total_cost = price_of_pens + price_of_markers + price_of_detergent
needed_money = total_cost - (total_cost * discount)
print(needed_money)
