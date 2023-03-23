age = input()
adults = 0
kids = 0

while age != "Christmas":
    age = int(age)

    if age <= 16:
        kids += 1
    elif age > 16:
        adults += 1

    age = input()

price_for_toys = kids * 5
price_for_sweaters = adults * 15

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {price_for_toys}")
print(f"Money for sweaters: {price_for_sweaters}")
