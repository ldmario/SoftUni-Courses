list_of_numbers = input().split(", ")
beggars = int(input())
final_list = []
counter = 0

my_list = []
for current_index in list_of_numbers:
    my_list.append(int(current_index))

while counter < beggars:
    beggars_sum = 0

    for current_index in range(counter, len(list_of_numbers), beggars):
        beggars_sum += my_list[current_index]
    counter += 1
    final_list.append(beggars_sum)

print(final_list)
