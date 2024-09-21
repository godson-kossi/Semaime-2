import random

def random_word_from_file(filename):
    """Reads a file and returns a random word from it."""
    try:
        with open(filename, 'r') as file:
            words = [line.strip().upper() for line in file if line.strip()]
        if not words:
            raise ValueError("The file is empty or contains no valid words.")
        return random.choice(words)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        raise
    except ValueError as e:
        print(f"Error: {e}")
        raise

def display_word(word, guesses):
    return ' '.join([letter if letter in guesses else '_' for letter in word])

def suggest_letter(word, guesses):
    frequency_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    for letter in frequency_order:
        if letter not in guesses and letter in word:
            return letter
    return None

def hangman_game(filename=None, cheat_mode=False):
    if filename:
        word_to_guess = random_word_from_file(filename)
    else:
        print("Error: No filename provided for word list.")
        return

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
