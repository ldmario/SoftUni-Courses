stadium_capacity = int(input())
number_of_fans = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0
for _ in range(1, number_of_fans + 1):
    sector = input()
    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1

perc_a = sector_a / number_of_fans * 100
perc_b = sector_b / number_of_fans * 100
perc_v = sector_v / number_of_fans * 100
perc_g = sector_g / number_of_fans * 100
perc_stadium_capacity_taken = number_of_fans / stadium_capacity * 100

print(f"{perc_a:.2f}%")
print(f"{perc_b:.2f}%")
print(f"{perc_v:.2f}%")
print(f"{perc_g:.2f}%")
print(f"{perc_stadium_capacity_taken:.2f}%")
