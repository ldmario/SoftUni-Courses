total_sum = 0

while True:
    current_sum = input()
    if current_sum == "NoMoreMoney":
        break
    else:
        current_sum = float(current_sum)
        if current_sum < 0:
            print("Invalid operation!")
            break
        else:
            total_sum += current_sum
            print(f"Increase: {current_sum:.2f}")
print(f"Total: {total_sum:.2f}")
