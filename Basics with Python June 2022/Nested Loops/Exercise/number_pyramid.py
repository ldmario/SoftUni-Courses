n = int(input())
current_number = 0
current_number_bigger_than_n = False
for row in range(1, n + 1):
    for col in range(1, row + 1):
        if current_number >= n:
            current_number_bigger_than_n = True
            break
        current_number += 1
        print(f"{current_number}", end=" ")
    if current_number_bigger_than_n:
        break
    print()
