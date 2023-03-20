number_of_orders = int(input())
total_price = 0

for order in range(number_of_orders):
    piece_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if not 0.01 <= piece_per_capsule <= 100.0 or not 1 <= days <= 31 or not 1 <= capsules_needed_per_day <= 2000:
        continue

    price = (days * capsules_needed_per_day) * piece_per_capsule
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price
else:
    print(f"Total: ${total_price:.2f}")
