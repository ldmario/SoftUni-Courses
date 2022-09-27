name = input()
grade = 1
total_grades = 0
failed = 2
while True:
    current_grade = float(input())
    if current_grade < 4.00:
        failed -= 1
        if failed == 0:
            print(f"{name} has been excluded at {grade} grade")
            break
        else:
            continue
    elif current_grade >= 4.00:
        if grade < 12:
            total_grades += current_grade
            grade += 1
        else:
            total_grades += current_grade
            break

average_grades = total_grades / grade
if grade == 12:
    print(f"{name} graduated. Average grade: {average_grades:.2f}")
