number_of_cargo = int(input())
tone_van = 0
tone_truck = 0
tone_train = 0
total_tones = 0
for cargo in range(1, number_of_cargo + 1):
    tone_of_one_cargo = int(input())
    total_tones += tone_of_one_cargo
    if tone_of_one_cargo <= 3:
        tone_van += tone_of_one_cargo
    elif 4 <= tone_of_one_cargo <= 11:
        tone_truck += tone_of_one_cargo
    elif 12 <= tone_of_one_cargo:
        tone_train += tone_of_one_cargo

average_price = (tone_van * 200 + tone_truck * 175 + tone_train * 120) / total_tones
percent_van = tone_van / total_tones * 100
percent_truck = tone_truck / total_tones * 100
percent_train = tone_train / total_tones * 100

print(f"{average_price:.2f}")
print(f"{percent_van:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")
