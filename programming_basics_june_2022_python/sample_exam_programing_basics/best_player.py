player_name = input()
best_player = ""
current_best_score = 0

while player_name != "END":
    realised_goals = int(input())

    if realised_goals > current_best_score:
        current_best_score = realised_goals
        best_player = player_name

    if realised_goals >= 10:
        break

    player_name = input()

print(f"{best_player} is the best player!")

if 3 <= current_best_score:
    print(f"He has scored {current_best_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {current_best_score} goals.")
