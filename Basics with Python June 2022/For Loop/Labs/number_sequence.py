from sys import maxsize

number = int(input())
n_max = -maxsize
n_min = maxsize

for n in range(1, number + 1):
    num = int(input())
    if num > n_max:
        n_max = num
    if num < n_min:
        n_min = num

print(f"Max number: {n_max}")
print(f"Min number: {n_min}")
