loops = int(input())
percent_1 = 0
percent_2 = 0
percent_3 = 0
percent_4 = 0
percent_5 = 0

for i in range(loops):
    current_number = int(input())
    if current_number < 200:
        percent_1 += 1 / loops * 100
    elif 200 <= current_number <= 399:
        percent_2 += 1 / loops * 100
    elif 400 <= current_number <= 599:
        percent_3 += 1 / loops * 100
    elif 600 <= current_number <= 799:
        percent_4 += 1 / loops * 100
    elif current_number >= 800:
        percent_5 += 1 / loops * 100

print(f"{percent_1:.2f}%")
print(f"{percent_2:.2f}%")
print(f"{percent_3:.2f}%")
print(f"{percent_4:.2f}%")
print(f"{percent_5:.2f}%")
