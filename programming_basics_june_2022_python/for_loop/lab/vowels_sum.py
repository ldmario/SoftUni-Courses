word = input()
total_sum = 0
for char in word:
    if char == "a":
        total_sum += 1
    if char == "e":
        total_sum += 2
    if char == "i":
        total_sum += 3
    if char == "o":
        total_sum += 4
    if char == "u":
        total_sum += 5

print(total_sum)
