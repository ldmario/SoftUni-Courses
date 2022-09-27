price_luggage_more_20_kg = float(input())
luggage_kilograms = float(input())
days_left_to_flight = int(input())
quantity_luggage = int(input())

total_price = 0

if luggage_kilograms < 10:
    total_price = price_luggage_more_20_kg * 0.2
elif 10 <= luggage_kilograms <= 20:
    total_price = price_luggage_more_20_kg / 2
elif luggage_kilograms > 20:
    total_price = price_luggage_more_20_kg

if days_left_to_flight > 30:
    total_price *= 1.10
elif 7 <= days_left_to_flight <= 30:
    total_price *= 1.15
elif days_left_to_flight < 7:
    total_price *= 1.40

total_price *= quantity_luggage

print(f" The total price of bags is: {total_price:.2f} lv.")
