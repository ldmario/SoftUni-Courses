couples_quantity = int(input())

couple = int(input()) + int(input())
diff = 0

for _ in range(1, couples_quantity):
    next_couple = int(input()) + int(input())
    if next_couple != couple:
        if diff < abs(couple - next_couple):
            diff = abs(couple - next_couple)
    couple = next_couple
if diff == 0:
    print(f"Yes, value={couple}")
else:
    print(f"No, maxdiff={diff}")
