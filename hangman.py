#!/usr/bin/env python3
"""
Hangman Word Guessing Game (Console)
------------------------------------
- 6 incorrect attempts allowed
- ASCII gallows art updates after each wrong guess
- Tracks guessed letters (no penalty for repeated guesses)
- Loads words from 'words.txt' if present, otherwise uses a built-in list
"""

import os
import random

MAX_ATTEMPTS = 6
WORDS_FILE = "words.txt"

# Fallback word list (used if words.txt is not found)
DEFAULT_WORDS = [
    "python", "programming", "variable", "function", "algorithm",
    "keyboard", "internet", "developer", "database", "network",
    "software", "hardware", "computer", "terminal", "library",
    "module", "string", "integer", "boolean", "compiler",
    "debugging", "backend", "frontend", "internship", "challenge",
]

# One ASCII picture per number of wrong guesses (0 to 6)
HANGMAN_STAGES = [
    # 0 wrong
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    # 1 wrong
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    # 2 wrong
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    # 3 wrong
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    # 4 wrong
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    # 5 wrong
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    # 6 wrong (game over)
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========""",
]


def load_words(filename=WORDS_FILE):
    """Load words from a text file (one per line). Fall back to DEFAULT_WORDS."""
    if os.path.isfile(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                words = [w.strip().lower() for w in f if w.strip().isalpha() and len(w.strip()) >= 4]
            if words:
                return words
        except OSError:
            pass
    return DEFAULT_WORDS


def choose_word(words):
    """Pick a random secret word."""
    return random.choice(words)


def get_masked_word(secret, guessed):
    """Return the word with unguessed letters hidden, e.g. '_ A _ H E O N'."""
    return " ".join(ch.upper() if ch in guessed else "_" for ch in secret)


def display_game(secret, guessed, wrong_count):
    """Print the gallows, masked word, wrong letters and attempts left."""
    wrong_letters = sorted(ch for ch in guessed if ch not in secret)
    print(HANGMAN_STAGES[wrong_count])
    print(f"\n  Word: {get_masked_word(secret, guessed)}")
    print(f"  Wrong guesses: {' '.join(l.upper() for l in wrong_letters) or '-'}")
    print(f"  Attempts left: {MAX_ATTEMPTS - wrong_count}\n")


def get_guess(guessed):
    """Ask for a valid single letter that has not been guessed before."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("  Please enter a single letter (A-Z).")
        elif guess in guessed:
            print(f"  You already guessed '{guess.upper()}'. Try a different letter.")
        else:
            return guess


def show_victory(secret, wrong_count):
    print("\n" + "=" * 44)
    print("   *** CONGRATULATIONS! YOU WON! ***")
    print(f"   The word was: {secret.upper()}")
    print(f"   Mistakes made: {wrong_count}/{MAX_ATTEMPTS}")
    print("=" * 44)


def show_defeat(secret):
    print(HANGMAN_STAGES[MAX_ATTEMPTS])
    print("\n" + "=" * 44)
    print("   xxx GAME OVER! YOU LOST! xxx")
    print(f"   The word was: {secret.upper()}")
    print("=" * 44)


def play_round(words):
    """Play one full game of Hangman."""
    secret = choose_word(words)
    guessed = set()  # all letters tried (correct and wrong)
    wrong_count = 0

    print("\n" + "=" * 44)
    print("        HANGMAN - Guess the hidden word!")
    print("=" * 44)

    while wrong_count < MAX_ATTEMPTS:
        display_game(secret, guessed, wrong_count)

        # Win check: every letter of the secret has been guessed
        if all(ch in guessed for ch in secret):
            show_victory(secret, wrong_count)
            return

        guess = get_guess(guessed)
        guessed.add(guess)

        if guess in secret:
            print(f"\n  Good job! '{guess.upper()}' is in the word.")
        else:
            wrong_count += 1
            print(f"\n  Sorry, '{guess.upper()}' is not in the word.")

        # Check win right after a correct guess (so we skip an extra prompt)
        if all(ch in guessed for ch in secret):
            display_game(secret, guessed, wrong_count)
            show_victory(secret, wrong_count)
            return

    show_defeat(secret)


def ask_play_again():
    while True:
        answer = input("\nPlay again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("  Please type 'y' or 'n'.")


def main():
    words = load_words()
    while True:
        play_round(words)
        if not ask_play_again():
            print("\nThanks for playing Hangman. Goodbye!")
            break


if __name__ == "__main__":
    main()
