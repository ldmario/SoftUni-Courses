expected_sum = int(input())
money_earned = 0
payment_counter = 0
payment_cash = 0
payment_cash_counter = 0
payment_card = 0
payment_card_counter = 0
average_card_payment = 0
average_cash_payment = 0
while money_earned < expected_sum:
    command = input()
    if command == "End":
        break
    command = int(command)
    payment_counter += 1
    if payment_counter % 2 == 0:
        if command >= 10:
            payment_card_counter += 1
            payment_card += command
            money_earned += command
            print("Product sold!")
        else:
            print("Error in transaction!")
    else:
        if command <= 100:
            payment_cash_counter += 1
            payment_cash += command
            money_earned += command
            print("Product sold!")
        else:
            print("Error in transaction!")
if payment_cash_counter != 0:
    average_cash_payment = payment_cash / payment_cash_counter
if payment_card_counter != 0:
    average_card_payment = payment_card / payment_card_counter

if money_earned >= expected_sum:
    print(f"Average CS: {average_cash_payment:.2f}")
    print(f"Average CC: {average_card_payment:.2f}")
else:
    print("Failed to collect required money for charity.")
