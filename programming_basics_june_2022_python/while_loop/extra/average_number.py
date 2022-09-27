n = int(input())
num_sum = 0

for number in range(n):
    num = int(input())
    num_sum += num

average_num = num_sum / n
print(f"{average_num:.2f}")
