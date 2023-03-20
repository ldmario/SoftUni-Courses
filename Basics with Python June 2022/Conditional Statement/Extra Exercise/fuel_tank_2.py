type_fuel = input().lower()
liters = float(input())
card = input().lower()

if type_fuel == "diesel" and card == "yes":
    if liters < 20:
        total_sum = liters * (2.33 - 0.12)
        print(f"{total_sum:.2f} lv.")
    elif 20 <= liters <= 25:
        total_sum = liters * (2.33 - 0.12)
        total_sum *= 0.92
        print(f"{total_sum:.2f} lv.")
    elif liters > 25:
        total_sum = liters * (2.33 - 0.12)
        total_sum *= 0.90
        print(f"{total_sum:.2f} lv.")
else:
    if type_fuel == "diesel" and card == "no":
        if liters < 20:
            total_sum = liters * 2.33
            print(f"{total_sum:.2f} lv.")
        elif 20 <= liters <= 25:
            total_sum = liters * 2.33
            total_sum *= 0.92
            print(f"{total_sum:.2f} lv.")
        elif liters > 25:
            total_sum = liters * 2.33
            total_sum *= 0.90
            print(f"{total_sum:.2f} lv.")
    else:
        if type_fuel == "gasoline" and card == "yes":
            if liters < 20:
                total_sum = liters * (2.22 - 0.18)
                print(f"{total_sum:.2f} lv.")
            elif 20 <= liters <= 25:
                total_sum = liters * (2.22 - 0.18)
                total_sum *= 0.92
                print(f"{total_sum:.2f} lv.")
            elif liters > 25:
                total_sum = liters * (2.22 - 0.18)
                total_sum *= 0.90
                print(f"{total_sum:.2f} lv.")
        else:
            if type_fuel == "gasoline" and card == "no":
                if liters < 20:
                    total_sum = liters * 2.22
                    print(f"{total_sum:.2f} lv.")
                elif 20 <= liters <= 25:
                    total_sum = liters * 2.22
                    total_sum *= 0.92
                    print(f"{total_sum:.2f} lv.")
                elif liters > 25:
                    total_sum = liters * 2.22
                    total_sum *= 0.90
                    print(f"{total_sum:.2f} lv.")
            else:
                if type_fuel == "gas" and card == "yes":
                    if liters < 20:
                        total_sum = liters * (0.93 - 0.08)
                        print(f"{total_sum:.2f} lv.")
                    elif 20 <= liters <= 25:
                        total_sum = liters * (0.93 - 0.08)
                        total_sum *= 0.92
                        print(f"{total_sum:.2f} lv.")
                    elif liters > 25:
                        total_sum = liters * (0.93 - 0.08)
                        total_sum *= 0.90
                        print(f"{total_sum:.2f} lv.")
                else:
                    if type_fuel == "gas" and card == "no":
                        if liters < 20:
                            total_sum = liters * 0.93
                            print(f"{total_sum:.2f} lv.")
                        elif 20 <= liters <= 25:
                            total_sum = liters * 0.93
                            total_sum *= 0.92
                            print(f"{total_sum:.2f} lv.")
                        elif liters > 25:
                            total_sum = liters * 0.93
                            total_sum *= 0.90
                            print(f"{total_sum:.2f} lv.")
