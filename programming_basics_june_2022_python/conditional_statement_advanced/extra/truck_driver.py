season = input().lower()
km_per_month = float(input())
salary = 0
if km_per_month <= 5000:
    if season == "spring" or season == "autumn":
        salary = km_per_month * 0.75 * 0.90 * 4
    elif season == "summer":
        salary = km_per_month * 0.90 * 0.90 * 4
    elif season == "winter":
        salary = km_per_month * 1.05 * 0.90 * 4
elif 5000 < km_per_month <= 10000:
    if season == "spring" or season == "autumn":
        salary = km_per_month * 0.95 * 0.90 * 4
    elif season == "summer":
        salary = km_per_month * 1.10 * 0.90 * 4
    elif season == "winter":
        salary = km_per_month * 1.25 * 0.90 * 4
elif 10000 < km_per_month <= 20000:
    if season == "spring" or season == "autumn" or season == "summer" or season == "winter":
        salary = km_per_month * 1.45 * 0.90 * 4

print(f"{salary:.2f}")
