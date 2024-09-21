# Task 1 
# Let’s develop a hangman game engine.
# The objective is to guess a word (randomly picked from a list) with the minimum of penalties.
# The player must suggest a letter at each turn.
# ✓ if the word contains this letter, the occurrences of the letter are revealed and the player gets 1 penalty;
# ✓ if the word does not contain this letter, the player gets 3
# penalties.
# At any time, the player can propose a full word.
# If the word is the one to be guessed, the player wins.
# Else, the player gets 5 penalties.


# import random

# def random_word():
#     word_list = ["Tom", "hangman", "Alexandre", "Victor", "Constant", "Kossi", "Belinda", "Arthur", "Leo", "Jaures"]
#     return random.choice(word_list).upper()

# def display_word(word, guesses):
#     return ' '.join([letter if letter in guesses else '_' for letter in word])

# def hangman_game():
#     word_to_guess = random_word()
#     guesses = set()
#     penalties = 0
#     guessed_word = False

#     print(display_word(word_to_guess, guesses) + f" / {penalties} penalties")

#     while not guessed_word:
#         guess = input("Enter a letter or guess the full word: ").strip().upper()

#         if len(guess) == 1:
#             if guess in word_to_guess:
#                 occurrences = word_to_guess.count(guess)
#                 guesses.add(guess)
#                 penalties += 1
#                 print(f"Found {occurrences} '{guess}'")
#             else:
#                 penalties += 3
#                 print(f"No '{guess}' found")
#         elif len(guess) == len(word_to_guess):
#             if guess == word_to_guess:
#                 guessed_word = True
#                 print(f"{guess}: correct guess!")
#             else:
#                 penalties += 5
#                 print(f"{guess}: incorrect guess")
#         else:
#             print("Invalid guess, try again.")

#         print(display_word(word_to_guess, guesses) + f" / {penalties} penalties")

#         if all(letter in guesses for letter in word_to_guess):
#             guessed_word = True
#             print(f"{word_to_guess}: You've guessed the word!")

#     print(f"Game Over! You finished with {penalties} penalties.")

# if __name__ == "__main__":
#     hangman_game()


# Task 2
#If you feel over-confident, add a cheat mode by developing a little AI engine.


import random
import sys

def random_word():
    word_list = ["Tom", "hangman", "Alexandre", "Victor", "Constant", "Kossi", "Belinda", "Arthur", "Leo", "Jaures"]
    return random.choice(word_list).replace(" ", "").upper()

def display_word(word, guesses):
    return ' '.join([letter if letter in guesses else '_' for letter in word])

def suggest_letter(word, guesses):
    frequency_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    for letter in frequency_order:
        if letter not in guesses and letter in word:
            return letter
    return None

def hangman_game(cheat_mode=False):
    word_to_guess = random_word()
    guesses = set()
    penalties = 0
    guessed_word = False

    print(display_word(word_to_guess, guesses) + f" / {penalties} penalties")

    while not guessed_word:
        if cheat_mode:
            advice = suggest_letter(word_to_guess, guesses)
            if advice:
                print(f"('{advice}' advised) ", end='')

        guess = input("Enter a letter or guess the full word: ").strip().upper()

        if len(guess) == 1:
            if guess in word_to_guess:
                occurrences = word_to_guess.count(guess)
                guesses.add(guess)
                penalties += 1
                print(f"Found {occurrences} '{guess}'")
            else:
                penalties += 3
                print(f"No '{guess}' found")
        elif len(guess) == len(word_to_guess):
            if guess == word_to_guess:
                guessed_word = True
                print(f"{guess}: correct guess!")
            else:
                penalties += 5
                print(f"{guess}: incorrect guess")
        else:
            print("Invalid guess, try again.")

        print(display_word(word_to_guess, guesses) + f" / {penalties} penalties")

        if all(letter in guesses for letter in word_to_guess):
            guessed_word = True
            print(f"{word_to_guess}: You've guessed the word!")

    print(f"Game Over! You finished with {penalties} penalties.")

if __name__ == "__main__":
    cheat_mode = '--cheat' in sys.argv
    hangman_game(cheat_mode)
