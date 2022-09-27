bad_grades = int(input())

amount_task = 0
total_scores = 0
last_task = ""
count_bad_grades = 0

while count_bad_grades < bad_grades:
    current_task = input()
    if current_task == "Enough":
        average_score = total_scores / amount_task
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {amount_task}")
        print(f"Last problem: {last_task}")
        break
    grade = int(input())
    if grade <= 4:
        count_bad_grades += 1

    amount_task += 1
    last_task = current_task
    total_scores += grade

if count_bad_grades == bad_grades:
    print(f"You need a break, {count_bad_grades} poor grades.")
