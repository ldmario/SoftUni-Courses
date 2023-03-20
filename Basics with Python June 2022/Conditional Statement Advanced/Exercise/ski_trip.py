days = int(input())
room_type = input()
evaluation = input()
nights = days - 1
total_price = 0

if room_type == "room for one person":
    total_price = 18.00 * nights
elif room_type == "apartment":
    if days < 10:
        total_price = (25.00 * nights) * 0.70
    elif 10 <= days <= 15:
        total_price = (25.00 * nights) * 0.65
    elif days > 15:
        total_price = (25.00 * nights) * 0.50
elif room_type == "president apartment":
    if days < 10:
        total_price = (35.00 * nights) * 0.90
    elif 10 <= days <= 15:
        total_price = (35.00 * nights) * 0.85
    elif days > 15:
        total_price = (35.00 * nights) * 0.80
if evaluation == "positive":
    total_price *= 1.25
else:
    total_price *= 0.90

print(f"{total_price:.2f}")
