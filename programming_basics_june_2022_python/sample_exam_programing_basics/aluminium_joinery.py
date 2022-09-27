quantity_joinery = int(input())
kind_joinery = input()
type_receive = input()

order_sum = 0

if kind_joinery == "90X130":
    order_sum = 110 * quantity_joinery
    if 30 < quantity_joinery <= 60:
        order_sum *= 0.95
    elif quantity_joinery > 60:
        order_sum *= 0.92
elif kind_joinery == "100X150":
    order_sum = 140 * quantity_joinery
    if 40 < quantity_joinery <= 80:
        order_sum *= 0.94
    elif quantity_joinery > 80:
        order_sum *= 0.90
elif kind_joinery == "130X180":
    order_sum = 190 * quantity_joinery
    if 20 < quantity_joinery <= 50:
        order_sum *= 0.93
    elif quantity_joinery > 50:
        order_sum *= 0.88
elif kind_joinery == "200X300":
    order_sum = 250 * quantity_joinery
    if 25 < quantity_joinery <= 50:
        order_sum *= 0.91
    elif quantity_joinery > 50:
        order_sum *= 0.86

if type_receive == "With delivery":
    order_sum += 60

if quantity_joinery > 99:
    order_sum *= 0.96

if quantity_joinery < 10:
    print("Invalid order")
else:
    print(f"{order_sum:.2f} BGN")
