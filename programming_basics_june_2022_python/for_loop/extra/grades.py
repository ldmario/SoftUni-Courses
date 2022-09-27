students_quantity = int(input())
total_evaluation = 0
weak = 0
medium = 0
good = 0
excellent = 0

for _ in range(students_quantity):
    evaluation = float(input())
    total_evaluation += evaluation
    if 2.00 <= evaluation <= 2.99:
        weak += 1
    elif 3.00 <= evaluation <= 3.99:
        medium += 1
    elif 4.00 <= evaluation <= 4.99:
        good += 1
    elif evaluation >= 5:
        excellent += 1

average_evaluation = total_evaluation / students_quantity
perc_weak = weak / students_quantity * 100
perc_medium = medium / students_quantity * 100
perc_good = good / students_quantity * 100
perc_excellent = excellent / students_quantity * 100

print(f"Top students: {perc_excellent:.2f}%")
print(f"Between 4.00 and 4.99: {perc_good:.2f}%")
print(f"Between 3.00 and 3.99: {perc_medium:.2f}%")
print(f"Fail: {perc_weak:.2f}%")
print(f"Average: {average_evaluation:.2f}")
