budget = float(input())
season = input()
class_car = ""
type_car = ""
car_price = 0

if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        car_price = budget * 0.35
    elif season == "Winter":
        type_car = "Jeep"
        car_price = budget * 0.65
elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        car_price = budget * 0.45
    elif season == "Winter":
        type_car = "Jeep"
        car_price = budget * 0.80
elif budget > 500:
    class_car = "Luxury class"
    car_price = budget * 0.90
    if season == "Summer" or season == "Winter":
        type_car = "Jeep"

print(f"{class_car}")
print(f"{type_car} - {car_price:.2f}")
