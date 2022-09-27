season = input()
kind_group = input()
students = int(input())
nights = int(input())
price = 0
sport = ""

if season == "Winter":
    if kind_group == "girls":
        sport = "Gymnastics"
        price = students * nights * 9.60
    elif kind_group == "boys":
        sport = "Judo"
        price = students * nights * 9.60
    elif kind_group == "mixed":
        sport = "Ski"
        price = students * nights * 10
    if students >= 50:
        price *= 0.50
    elif 20 <= students < 50:
        price *= 0.85
    elif 10 <= students < 20:
        price *= 0.95
elif season == "Spring":
    if kind_group == "boys":
        sport = "Tennis"
        price = students * nights * 7.20
    elif kind_group == "girls":
        sport = "Athletics"
        price = students * nights * 7.20
    elif kind_group == "mixed":
        sport = "Cycling"
        price = students * nights * 9.50
    if students >= 50:
        price *= 0.50
    elif 20 <= students < 50:
        price *= 0.85
    elif 10 <= students < 20:
        price *= 0.95
elif season == "Summer":
    if kind_group == "boys":
        sport = "Football"
        price = students * nights * 15
    elif kind_group == "girls":
        sport = "Volleyball"
        price = students * nights * 15
    elif kind_group == "mixed":
        sport = "Swimming"
        price = students * nights * 20
    if students >= 50:
        price *= 0.50
    elif 20 <= students < 50:
        price *= 0.85
    elif 10 <= students < 20:
        price *= 0.95

print(f"{sport} {price:.2f} lv.")
