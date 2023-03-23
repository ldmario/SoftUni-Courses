type_projection = input()
rows = int(input())
columns = int(input())
income = 0
capacity = rows * columns

if type_projection == "Premiere":
    income = capacity * 12.00
elif type_projection == "Normal":
    income = capacity * 7.50
elif type_projection == "Discount":
    income = capacity * 5.00

print(f"{income:.2f} leva")
