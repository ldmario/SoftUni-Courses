amount_of_students = int(input())
result_excellent = 0
result_very_good = 0
result_good = 0
result_medium = 0
total_scores = 0

for _ in range(amount_of_students):
    result = float(input())
    total_scores += result
    if result >= 5.00:
        result_excellent += 1
    elif 4.00 <= result < 5.00:
        result_very_good += 1
    elif 3.00 <= result < 4.00:
        result_good += 1
    elif 2.00 <= result < 3.00:
        result_medium += 1

average_score = total_scores / amount_of_students
perc_result_excellent = result_excellent * 100 / amount_of_students
perc_result_very_good = result_very_good * 100 / amount_of_students
perc_result_good = result_good * 100 / amount_of_students
perc_result_medium = result_medium * 100 / amount_of_students

print(f"Top students: {perc_result_excellent:.2f}%")
print(f"Between 4.00 and 4.99: {perc_result_very_good:.2f}%")
print(f"Between 3.00 and 3.99: {perc_result_good:.2f}%")
print(f"Fail: {perc_result_medium:.2f}%")
print(f"Average: {average_score:.2f}")
