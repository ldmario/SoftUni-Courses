quantity_locations = int(input())

for locations in range(quantity_locations):

    total_yield = 0

    average_expected_yield = int(input())
    amount_of_days_yield = int(input())

    for day in range(amount_of_days_yield):

        current_yield = int(input())
        total_yield += current_yield

    average_yield = total_yield / amount_of_days_yield

    if average_expected_yield <= average_yield:
        print(f"Good job! Average gold per day: {average_yield:.2f}.")
    elif average_expected_yield > average_yield:
        diff = abs(average_expected_yield - average_yield)
        print(f"You need {diff:.2f} gold.")
