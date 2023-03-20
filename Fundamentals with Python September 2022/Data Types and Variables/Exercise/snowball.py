number_of_snowballs = int(input())
highest_quality = 0
current_weight = 0
current_time = 0
current_quality = 0

for _ in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality_of_snowball = int(input())

    current_ball_quality = int((weight / time) ** quality_of_snowball)

    if current_ball_quality > highest_quality:
        highest_quality = current_ball_quality
        current_weight = weight
        current_time = time
        current_quality = quality_of_snowball

print(f"{current_weight} : {current_time} = {highest_quality} ({current_quality})")
