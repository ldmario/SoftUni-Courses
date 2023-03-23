from sys import maxsize

loops = int(input())
total_sum = 0
highest_num = -maxsize

for num in range(1, loops + 1):
    current_num = int(input())
    total_sum += current_num
    if current_num > highest_num:
        highest_num = current_num

diff = abs(highest_num - (total_sum - highest_num))

if highest_num == total_sum - highest_num:
    print("Yes")
    print(f"Sum = {highest_num}")
else:
    print("No")
    print(f"Diff = {diff}")
