amount_of_ppl = int(input())
capacity_elevator = int(input())

amount_of_courses = int(amount_of_ppl / capacity_elevator)

if amount_of_ppl % capacity_elevator != 0:
    amount_of_courses += 1

print(amount_of_courses)
