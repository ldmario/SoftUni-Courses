deposit_sum = float(input())
interval_of_deposit = int(input())
annual_interest_rate = float(input())
percentage_interest = annual_interest_rate / 100
total_sum = deposit_sum + interval_of_deposit * ((deposit_sum * percentage_interest) / 12)
print(total_sum)
