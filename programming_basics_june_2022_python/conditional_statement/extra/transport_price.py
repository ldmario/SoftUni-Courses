amount_kilometers = int(input())
tariff = input()

if amount_kilometers < 20 and tariff == "day":
    price_taxi = 0.70 + amount_kilometers * 0.79
    print(f"{price_taxi:.2f}")
elif amount_kilometers < 20 and tariff == "night":
    price_taxi = 0.70 + amount_kilometers * 0.90
    print(f"{price_taxi:.2f}")
elif 20 <= amount_kilometers < 100:
    price_bus = amount_kilometers * 0.09
    print(f"{price_bus:.2f}")
elif amount_kilometers >= 100:
    price_train = amount_kilometers * 0.06
    print(f"{price_train:.2f}")
