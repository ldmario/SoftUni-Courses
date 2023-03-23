from math import floor      # импортираме закръгляне на цяло число към по - малката стойност

record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_one_meter_in_seconds = float(input())

time_whole_distance_seconds = distance_in_meters * time_for_one_meter_in_seconds
resistance = floor(distance_in_meters / 15) * 12.5
total_time_needed = time_whole_distance_seconds + resistance
difference = abs(record_in_seconds - total_time_needed)

if total_time_needed < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time_needed:.2f} seconds.")
elif total_time_needed >= record_in_seconds:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
