number_free_days = int(input())
working_days = 365 - number_free_days
playing_in_free_days = number_free_days * 127   # minutes playing in free days
playing_in_work_days = working_days * 63    # minutes playing in working days
total_time_playing = playing_in_work_days + playing_in_free_days
difference_of_norm = abs(30000 - total_time_playing)
convert_in_hours = difference_of_norm // 60
convert_in_minutes = difference_of_norm % 60

if total_time_playing >= 30000:
    print(f'''Tom will run away
{convert_in_hours} hours and {convert_in_minutes} minutes more for play''')
else:
    print(f'''Tom sleeps well
{convert_in_hours} hours and {convert_in_minutes} minutes less for play''')
