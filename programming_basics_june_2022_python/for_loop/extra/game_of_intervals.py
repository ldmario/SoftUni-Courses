number_of_moves = int(input())
invalid_numbers = 0
total_nums = 0
result = 0
interval_0_9 = 0
interval_10_19 = 0
interval_20_29 = 0
interval_30_39 = 0
interval_40_49 = 0

for number in range(1, number_of_moves + 1):
    num = int(input())
    total_nums += 1
    if num > 50 or num <= -1:
        invalid_numbers += 1
        result /= 2
    elif 0 <= num <= 9:
        result += num * 0.20
        interval_0_9 += 1
    elif 10 <= num <= 19:
        result += num * 0.30
        interval_10_19 += 1
    elif 20 <= num <= 29:
        result += num * 0.40
        interval_20_29 += 1
    elif 30 <= num <= 39:
        result += 50
        interval_30_39 += 1
    elif 40 <= num <= 50:
        result += 100
        interval_40_49 += 1

perc_0_9 = interval_0_9 / total_nums * 100
perc_10_19 = interval_10_19 / total_nums * 100
perc_20_29 = interval_20_29 / total_nums * 100
perc_30_39 = interval_30_39 / total_nums * 100
perc_40_49 = interval_40_49 / total_nums * 100
perc_invalid_numbers = invalid_numbers / total_nums * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {perc_0_9:.2f}%")
print(f"From 10 to 19: {perc_10_19:.2f}%")
print(f"From 20 to 29: {perc_20_29:.2f}%")
print(f"From 30 to 39: {perc_30_39:.2f}%")
print(f"From 40 to 50: {perc_40_49:.2f}%")
print(f"Invalid numbers: {perc_invalid_numbers:.2f}%")
