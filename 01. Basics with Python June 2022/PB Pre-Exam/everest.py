days_count = 1
total_height = 8848
current_height = 5364
command = input()

while command != "END":
    if command == "Yes":
        days_count += 1

    if days_count > 5:
        break

    claimed_meters = int(input())
    current_height += claimed_meters

    if current_height >= total_height:
        break

    command = input()

if current_height < total_height:
    print(f"Failed!")
    print(f"{current_height}")
else:
    print(f"Goal reached for {days_count} days!")
