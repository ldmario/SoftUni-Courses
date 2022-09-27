number = int(input())

for num in range(1, number + 1):
    first_num = num // 10
    second_num = num % 10
    sum = int(first_num + second_num)
    if sum == 5 or sum == 7 or sum == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
