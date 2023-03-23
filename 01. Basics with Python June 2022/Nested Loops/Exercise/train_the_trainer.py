number_of_judges = int(input())
name_of_presentation = input()
total_score = 0
presentations_count = 0

while name_of_presentation != "Finish":
    score_of_current_presentation = 0
    average_score_of_current_presentation = 0
    presentations_count += 1

    for scores in range(1, number_of_judges + 1):
        current_score = float(input())
        score_of_current_presentation += current_score

        if scores == number_of_judges:
            average_score_of_current_presentation = score_of_current_presentation / number_of_judges
            total_score += average_score_of_current_presentation
            print(f"{name_of_presentation} - {average_score_of_current_presentation:.2f}.")

    name_of_presentation = input()

    if name_of_presentation == "Finish":
        total_average_score = total_score / presentations_count
        print(f"Student's final assessment is {total_average_score:.2f}.")
