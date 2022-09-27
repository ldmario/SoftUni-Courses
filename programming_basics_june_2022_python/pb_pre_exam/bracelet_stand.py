money_per_day = float(input())
money_from_sales = float(input())
spend = float(input())
gift_price = float(input())

pocket_money_for_five_days = money_per_day * 5
total_money_from_sales = money_from_sales * 5

total_saved_money = pocket_money_for_five_days + total_money_from_sales
total_money_after_spend = total_saved_money - spend

diff = abs(total_money_after_spend - gift_price)

if total_money_after_spend >= gift_price:
    print(f"Profit: {total_money_after_spend:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {diff:.2f} BGN.")
