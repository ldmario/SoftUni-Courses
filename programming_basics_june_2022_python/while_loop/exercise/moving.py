box_width = int(input())
box_length = int(input())
box_height = int(input())
total_cubic = box_length * box_width * box_height
cubic_left = total_cubic
taken_cubic = 0
while True:
    boxes = input()
    if not boxes == "Done":
        boxes = int(boxes)
        taken_cubic += boxes
        cubic_left -= boxes
        if cubic_left <= 0:
            break
    else:
        break

diff = abs(total_cubic - taken_cubic)

if 0 >= cubic_left:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")
