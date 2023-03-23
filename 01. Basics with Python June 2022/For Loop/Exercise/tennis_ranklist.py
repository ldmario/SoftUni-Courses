from math import floor

tournaments_participated = int(input())
start_points = int(input())

final_points = start_points
win_tournaments = 0

for _ in range(tournaments_participated):
    stage_of_tournament = input().lower()
    if stage_of_tournament == "w":
        win_tournaments += 1
        final_points += 2000
    elif stage_of_tournament == "f":
        final_points += 1200
    elif stage_of_tournament == "sf":
        final_points += 720

points_from_tournaments = final_points - start_points
average_points = points_from_tournaments / tournaments_participated
percent_win = win_tournaments * 100 / tournaments_participated

print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percent_win:.2f}%")
