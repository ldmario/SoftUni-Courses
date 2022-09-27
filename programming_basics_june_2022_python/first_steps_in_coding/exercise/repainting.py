needed_amount_of_nylon = int(input())
needed_amount_of_paint = int(input())
needed_amount_of_thinner = int(input())
hours_of_working = int(input())
sum_for_nylon = (needed_amount_of_nylon + 2) * 1.50
sum_for_paint = (needed_amount_of_paint + (needed_amount_of_paint * 0.10)) * 14.50
sum_for_thinner = needed_amount_of_thinner * 5.00
sum_for_bags = 0.40
total_sum = sum_for_nylon + sum_for_paint + sum_for_thinner + sum_for_bags
sum_for_one_hour_working = total_sum * 0.30
final_price = total_sum + (sum_for_one_hour_working * hours_of_working)
print(final_price)
