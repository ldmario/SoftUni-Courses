start_of_loop = int(input())
end_of_loop = int(input())
magic_number = int(input())
combination_no = 0
valid_combination = 0
for y in range(start_of_loop, end_of_loop + 1):
    for x in range(start_of_loop, end_of_loop + 1):
        combination_no += 1
        if y + x == magic_number:
            valid_combination += 1
            print(f"Combination N:{combination_no} ({y} + {x} = {magic_number})")
            break
    if valid_combination > 0:
        break
if valid_combination == 0:
    print(f"{combination_no} combinations - neither equals {magic_number}")
