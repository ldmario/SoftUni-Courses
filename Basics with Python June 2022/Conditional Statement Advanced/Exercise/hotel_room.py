month = input().lower()
numbers_of_nights = int(input())
price_studio = 0
price_apartment = 0
if month == "may" or month == "october":
    price_studio = 50
    price_apartment = 65
    if 7 < numbers_of_nights <= 14:
        price_studio *= 0.95
    elif numbers_of_nights > 14:
        price_studio *= 0.70
        price_apartment *= 0.90
elif month == "june" or month == "september":
    price_studio = 75.20
    price_apartment = 68.70
    if numbers_of_nights > 14:
        price_studio *= 0.80
        price_apartment *= 0.90
    pass
elif month == "july" or month == "august":
    price_studio = 76
    price_apartment = 77
    if numbers_of_nights > 14:
        price_apartment *= 0.90
total_studio = numbers_of_nights * price_studio
total_apartment = numbers_of_nights * price_apartment
print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")
