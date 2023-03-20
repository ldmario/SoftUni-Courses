number_of_lines = int(input())
open_brackets = False
balanced = None

for _ in range(number_of_lines):
    current_input = input()

    if current_input == "(":
        if open_brackets:
            balanced = False
            break
        else:
            open_brackets = True
    elif current_input == ")":
        if open_brackets:
            open_brackets = False
            balanced = True
            continue
        else:
            balanced = False
            break
    else:
        continue

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
