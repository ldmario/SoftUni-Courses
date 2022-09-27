exam_hour = int(input())
exam_minute = int(input())
hour_arrive = int(input())
minute_arrive = int(input())
exam_time_in_minutes = exam_hour * 60 + exam_minute
arrive_time_in_minutes = hour_arrive * 60 + minute_arrive
diff = exam_time_in_minutes - arrive_time_in_minutes
hour = 0
minutes = 0
if 0 <= diff <= 30:
    if diff == 0:
        print("On time")
    else:
        minutes = diff % 60
        print("On time")
        print(f"{minutes} minutes before the start")
elif diff > 30:
    hour = diff // 60
    minutes = diff % 60
    print("Early")
    if hour < 1:
        print(f"{minutes} minutes before the start")
    elif minutes < 10:
        print(f"{hour}:0{minutes} hours before the start")
    else:
        print(f"{hour}:{minutes} hours before the start")
elif diff < 0:
    diff = abs(diff)
    hour = diff // 60
    minutes = diff % 60
    print("Late")
    if hour < 1:
        print(f"{minutes} minutes after the start")
    elif minutes < 10:
        print(f"{hour}:0{minutes} hours after the start")
    else:
        print(f"{hour}:{minutes} hours after the start")
