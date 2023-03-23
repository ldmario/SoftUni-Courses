legacy_money = float(input())
year = int(input())

years_old = 18
money_needed = 0

for years in range(1800, year + 1):
    if years % 2 == 0:
        money_needed += 12000
        years_old += 1
    elif not years % 2 == 0:
        money_needed += 12000 + 50 * years_old
        years_old += 1

diff = abs(legacy_money - money_needed)

if money_needed <= legacy_money:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")
