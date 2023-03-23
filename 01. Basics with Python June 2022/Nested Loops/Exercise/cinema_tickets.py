total_tickets = 0
total_student_tickets = 0
total_standard_tickets = 0
total_kid_tickets = 0

name_of_movie = input()

while name_of_movie != "Finish":
    quantity_free_space = int(input())
    current_tickets = 0
    current_quantity = quantity_free_space

    while quantity_free_space > 0:
        type_of_ticket = input()
        if type_of_ticket == "End":
            break

        total_tickets += 1
        current_tickets += 1
        quantity_free_space -= 1

        if type_of_ticket == "student":
            total_student_tickets += 1
        elif type_of_ticket == "standard":
            total_standard_tickets += 1
        elif type_of_ticket == "kid":
            total_kid_tickets += 1

    perc_taken = current_tickets / current_quantity * 100
    print(f"{name_of_movie} - {perc_taken:.2f}% full.")
    name_of_movie = input()

perc_student = total_student_tickets / total_tickets * 100
perc_standard = total_standard_tickets / total_tickets * 100
perc_kids = total_kid_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{perc_student:.2f}% student tickets.")
print(f"{perc_standard:.2f}% standard tickets.")
print(f"{perc_kids:.2f}% kids tickets.")
