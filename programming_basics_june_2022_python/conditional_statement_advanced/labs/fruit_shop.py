fruit = input().lower()
day = input().lower()
quantity = float(input())
price = 0
if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
    else:
        print("error")
elif day == "saturday" or day == "sunday":
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
    else:
        print("error")
else:
    print("error")
if price > 0:
    total = price * quantity
    print(f"{total:.2f}")
