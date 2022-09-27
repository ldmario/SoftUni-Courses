bottles_detergent = int(input())
quantity_detergent = bottles_detergent * 750
detergent_left = quantity_detergent
plates_counter = 0
pots_counter = 0
input_counter = 0

while True:
    command = input()
    if command == "End":
        break
    command = int(command)
    input_counter += 1
    if input_counter % 3 == 0:
        pots_counter += command
        detergent_left -= command * 15
    else:
        plates_counter += command
        detergent_left -= command * 5
    if detergent_left < 0:
        break

if detergent_left >= 0:
    print("Detergent was enough!")
    print(f"{plates_counter} dishes and {pots_counter} pots were washed.")
    print(f"Leftover detergent {detergent_left} ml.")
else:
    diff = abs(detergent_left)
    print(f"Not enough detergent, {diff} ml. more necessary!")
