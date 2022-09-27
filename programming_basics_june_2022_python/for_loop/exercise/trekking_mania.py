number_groups = int(input())

total_people = 0
group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
group_5 = 0

for people in range(1, number_groups + 1):
    amount_people = int(input())
    total_people += amount_people
    if amount_people <= 5:
        group_1 += amount_people
    elif 5 < amount_people <= 12:
        group_2 += amount_people
    elif 12 < amount_people <= 25:
        group_3 += amount_people
    elif 25 < amount_people <= 40:
        group_4 += amount_people
    elif amount_people >= 41:
        group_5 += amount_people

perc_group_1 = group_1 * 100 / total_people
perc_group_2 = group_2 * 100 / total_people
perc_group_3 = group_3 * 100 / total_people
perc_group_4 = group_4 * 100 / total_people
perc_group_5 = group_5 * 100 / total_people

print(f"{perc_group_1:.2f}%")
print(f"{perc_group_2:.2f}%")
print(f"{perc_group_3:.2f}%")
print(f"{perc_group_4:.2f}%")
print(f"{perc_group_5:.2f}%")
