day = input().lower()

if day == "monday" or day == "tuesday" or day == "wednesday"\
     or day == "thursday" or day == "friday":
    print("Working day")
elif day == "saturday" or day == "sunday":
    print("Weekend")
else:
    print("Error")