hour = int(input())
day = input().lower()

if day == "monday" or day == "tuesday" or day == "wednesday"\
     or day == "thursday" or day == "friday" or day == "saturday":
    if 10 <= hour <= 18:
        print("open")
    else:
        print("closed")
elif day == "sunday":
    print("closed")
    