num = int(input())
valid_operations = 0

for x1 in range(num + 1):
    for x2 in range(num + 1):
        for x3 in range(num + 1):
            if x1 + x2 + x3 == num:
                valid_operations += 1

print(valid_operations)
