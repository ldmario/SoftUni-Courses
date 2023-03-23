budget = float(input())
season = input()
location = ""
type_of_accommodation = ""
price = 0

if budget <= 1000:
    type_of_accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45
elif 1000 < budget <= 3000:
    type_of_accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.60
elif budget > 3000:
    type_of_accommodation = "Hotel"
    price = budget * 0.90
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {type_of_accommodation} - {price:.2f}")
