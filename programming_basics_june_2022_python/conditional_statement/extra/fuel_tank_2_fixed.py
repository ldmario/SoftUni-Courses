type_fuel = input().lower()
liters = float(input())
card = input().lower()
total_sum = 0
if type_fuel == "diesel" and card == "yes":
    total_sum = liters * (2.33 - 0.12)
elif type_fuel == "diesel" and card == "no":
    total_sum = liters * 2.33
elif type_fuel == "gasoline" and card == "yes":
    total_sum = liters * (2.22 - 0.18)
elif type_fuel == "gasoline" and card == "no":
    total_sum = liters * 2.22
elif type_fuel == "gas" and card == "yes":
    total_sum = liters * (0.93 - 0.08)
elif type_fuel == "gas" and card == "no":
    total_sum = liters * 0.93

if liters < 20:
    print(f"{total_sum:.2f} lv.")
elif 20 <= liters <= 25:
    total_sum *= 0.92
    print(f"{total_sum:.2f} lv.")
elif liters > 25:
    total_sum *= 0.90
    print(f"{total_sum:.2f} lv.")
