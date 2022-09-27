import random

while True:
    words = ["snake", "airplane", "hospital", "airport", "executioner", "mosquito", "jazz", "zigzag", "kiwifruit",
             "zipper", "jogging", "joke", "strength", "whiskey", "exodus", "rhythm"]

    chosen_word = random.choice(words).lower()  # choosing a random word
    attempts = len(chosen_word) - 2     # possible attempts for guessing
    guessed_letters = []    # a list of letters guessed so far
    hidden_word = []     # storing the hidden word
    joined_word = None

    for letter in chosen_word:
        hidden_word.append('-')

    while attempts != 0 and '-' in hidden_word:

        if attempts == 0:
            break

        hidden_word[0] = chosen_word[0]     # reveals first letter from chosen_word
        hidden_word[len(hidden_word) - 1] = chosen_word[len(chosen_word) - 1]     # reveals last letter from chosen_word

        print(f"You have {attempts} attempts remaining!")
        print("Make your Guess from A - Z:")
        joined_word = ''.join(hidden_word)      # Joining the "-" from hidden_word list
        print(joined_word)
        player_guess = input("> ")

        if not player_guess.isalpha():
            print("Not a letter input. Try again!")
            continue
        elif len(player_guess) > 1:
            print("That is more than one letter. Try again!")
            continue
        elif player_guess in guessed_letters:
            print("You have already guessed that letter. Try again!")
            continue

        guessed_letters.append(player_guess)

        for index, letter in enumerate(chosen_word):        # replace player guess if letters exist
            if player_guess == letter:
                hidden_word[index] = player_guess

        if player_guess not in chosen_word:
            attempts -= 1

    if attempts == 0:
        print("You lose")
        print(f"Word was {chosen_word}")
    else:
        print(chosen_word)
        print("You win")

    another_game = input("One more game ?" + "\n>").lower()
    if another_game == "y" or another_game == "yes":
        continue
    else:
        print("Cya next time !")
        break
