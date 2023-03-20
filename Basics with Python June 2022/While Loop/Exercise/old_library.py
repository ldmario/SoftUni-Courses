fav_book = input()
count = 0
current_book = input()
while current_book != "No More Books":
    if current_book == fav_book:
        print(f"You checked {count} books and found it.")
        break

    count += 1
    current_book = input()

if current_book == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {count} books.")
