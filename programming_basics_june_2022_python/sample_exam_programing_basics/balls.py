quantity_balls = int(input())

total_points = 0
red_ball = 0
orange_ball = 0
yellow_ball = 0
white_ball = 0
other_colors = 0
black_ball = 0

for _ in range(quantity_balls):
    color = input()
    if color == "red":
        total_points += 5
        red_ball += 1
    elif color == "orange":
        total_points += 10
        orange_ball += 1
    elif color == "yellow":
        total_points += 15
        yellow_ball += 1
    elif color == "white":
        total_points += 20
        white_ball += 1
    elif color == "black":
        total_points /= 2
        black_ball += 1
    else:
        other_colors += 1

print(f"Total points: {int(total_points)}")
print(f"Red balls: {red_ball}")
print(f"Orange balls: {orange_ball}")
print(f"Yellow balls: {yellow_ball}")
print(f"White balls: {white_ball}")
print(f"Other colors picked: {other_colors}")
print(f"Divides from black balls: {black_ball}")
