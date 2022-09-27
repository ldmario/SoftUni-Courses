loop = int(input())
sum_odd = 0
sum_even = 0

for i in range(1, loop + 1):
    current_number = int(input())
    if i % 2 == 0:
        sum_even += current_number
    else:
        sum_odd += current_number

diff = abs(sum_odd - sum_even)

if sum_odd == sum_even:
    print("Yes")
    print(f"Sum = {sum_odd}")
else:
    print("No")
    print(f"Diff = {diff}")
