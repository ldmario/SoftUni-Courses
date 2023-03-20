def valid_password(password):
    def digit_counter():
        counter = 0
        for char in password:
            if char.isdigit():
                counter += 1
        if counter >= 2:
            return True
        else:
            return False

    def length_checker():
        if 6 <= len(password) <= 10:
            return True
        else:
            return False

    def non_special_symbols_checker():
        if password.isalnum():
            return True
        else:
            return False

    valid_criteria = 0
    if length_checker():
        valid_criteria += 1
    else:
        print("Password must be between 6 and 10 characters")
    if non_special_symbols_checker():
        valid_criteria += 1
    else:
        print("Password must consist only of letters and digits")
    if digit_counter():
        valid_criteria += 1
    else:
        print("Password must have at least 2 digits")

    if valid_criteria == 3:
        print("Password is valid")


current_password = input()
valid_password(current_password)
