current_string = input()

while current_string != "End":
    if current_string == "SoftUni":
        current_string = input()
        continue

    for char in current_string:
        print(char * 2, end="")
    print()
    current_string = input()
