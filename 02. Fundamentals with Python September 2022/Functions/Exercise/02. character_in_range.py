def character_in_range(a, b):
    chars = ""
    char1 = ord(a)
    char2 = ord(b)
    for char in range(char1 + 1, char2):
        chars += (chr(char)) + " "

    return chars


first_range = input()
second_range = input()

characters = character_in_range(first_range, second_range)

print(characters)
