lenght = float(input())
width = float(input())
lenght = lenght * 100
width = width * 100 - 100
number_of_places_in_a_row = width / 70
number_of_rows = lenght / 120
total_number_of_places = int(number_of_places_in_a_row) * int(number_of_rows) - 3
print(total_number_of_places)
