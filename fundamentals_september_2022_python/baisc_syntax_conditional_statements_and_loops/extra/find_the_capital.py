string = input()
upper_chars = []
for index, char in enumerate(string):
    if char.isupper():
        upper_chars.append(index)

print(upper_chars)
