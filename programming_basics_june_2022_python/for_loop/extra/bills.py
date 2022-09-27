months = int(input())

electricity = 0
water = 0
internet = 0
others = 0

for _ in range(1, months + 1):
    electricity_monthly = float(input())
    electricity += electricity_monthly
    water += 20
    internet += 15
    others += (electricity_monthly + 20 + 15) * 1.20

average_expenses = (electricity + water + internet + others) / months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average_expenses:.2f} lv")