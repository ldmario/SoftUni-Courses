day = input().lower()
ticket = 0

if day == "monday":
    ticket = 12
elif day == "tuesday":
    ticket = 12
elif day == "wednesday":
    ticket = 14
elif day == "thursday":
    ticket = 14
elif day == "friday":
    ticket = 12
elif day == "saturday":
    ticket = 16
elif day == "sunday":
    ticket = 16

print(ticket)
