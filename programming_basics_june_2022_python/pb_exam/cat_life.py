from math import floor

cat_breed = input()
cat_gender = input()

human_years = 0

if cat_breed == "British Shorthair":
    if cat_gender == "m":
        human_years = 13
    elif cat_gender == "f":
        human_years = 14
elif cat_breed == "Siamese":
    if cat_gender == "m":
        human_years = 15
    elif cat_gender == "f":
        human_years = 16
elif cat_breed == "Persian":
    if cat_gender == "m":
        human_years = 14
    elif cat_gender == "f":
        human_years = 15
elif cat_breed == "Ragdoll":
    if cat_gender == "m":
        human_years = 16
    elif cat_gender == "f":
        human_years = 17
elif cat_breed == "American Shorthair":
    if cat_gender == "m":
        human_years = 12
    elif cat_gender == "f":
        human_years = 13
elif cat_breed == "Siberian":
    if cat_gender == "m":
        human_years = 11
    elif cat_gender == "f":
        human_years = 12
else:
    print(f"{cat_breed} is invalid cat!")

human_months = human_years * 12
cat_months = human_months / 6
if human_years > 0:
    print(f"{floor(cat_months)} cat months")
