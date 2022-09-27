number_of_pages = int(input())
pages_for_hour = int(input())
amount_of_days = int(input())
total_time_needed = number_of_pages / pages_for_hour
needed_hours_per_day = total_time_needed / amount_of_days
print(int(needed_hours_per_day))
