from string import punctuation

alphabet = "abcdefghijklmnopqrstuvwxyz"
special_symbols = punctuation
hidden_command_c_counter = 0
hidden_command_o_counter = 0
hidden_command_n_counter = 0
hidden_word = ""
command = ""
while not command == "End":
    if hidden_command_o_counter == 1 and hidden_command_c_counter == 1 and hidden_command_n_counter == 1:
        print(f"{hidden_word}", end=' ')
        hidden_word = ""
        hidden_command_c_counter = 0
        hidden_command_o_counter = 0
        hidden_command_n_counter = 0
    command = input()
    if command in alphabet.lower() or command in alphabet.upper() and command not in special_symbols:
        if hidden_command_o_counter == 0 or hidden_command_c_counter == 0 or hidden_command_n_counter == 0:
            if command == "c" and hidden_command_c_counter != 1:
                hidden_command_c_counter += 1
            elif command == "o" and hidden_command_o_counter != 1:
                hidden_command_o_counter += 1
            elif command == "n" and hidden_command_n_counter != 1:
                hidden_command_n_counter += 1
            else:
                hidden_word += command
