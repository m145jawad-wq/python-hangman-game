# 🎮 Hangman Word Guessing Game (Console)

A terminal-based Hangman game built with Python 3. Guess the hidden word letter by letter within 6 attempts before the hangman is complete!

## ✨ Features

- 🎯 6 incorrect attempts allowed
- 🖼️ ASCII gallows art that updates after every wrong guess
- 🔤 Masked word display (e.g. `_ Y _ H O N`)
- 📝 Tracks all guessed letters using a Python `set`
- 🚫 No penalty for repeating an already guessed letter
- ✅ Input validation (accepts only a single alphabet letter)
- 🏆 Clean victory and defeat screens
- 🔁 Play again option
- 📂 Loads words from `words.txt` (falls back to a built-in word list)

## 🛠️ Tech Stack

- Python 3
- Standard Library (`random`, `os`)

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/m145jawad-wq/python-hangman-game.git
   cd python-hangman-game
   ```
2. (Optional) Place an English word list named `words.txt` in the same folder.
3. Run the game:
   ```bash
   python hangman.py
   ```

## 🕹️ How to Play

1. A random word is chosen and shown as underscores.
2. Enter one letter at a time.
3. Correct letters are revealed in the word.
4. Wrong letters add a part to the hangman.
5. Win by guessing the full word before 6 mistakes!

## 🖼️ Sample Gameplay

```
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========

  Word: _ Y _ H O N
  Wrong guesses: E X A
  Attempts left: 3

Guess a letter:
```

## 🧩 Code Structure

| Function | Purpose |
|---|---|
| `load_words()` | Loads words from file or default list |
| `choose_word()` | Picks a random secret word |
| `get_masked_word()` | Builds the hidden word display |
| `display_game()` | Shows gallows, word, and attempts left |
| `get_guess()` | Validates user input |
| `show_victory()` / `show_defeat()` | Win and lose screens |
| `play_round()` | Runs one full game |
| `main()` | Game loop with replay option |

## 📚 What I Learned

- String manipulation and control flow
- Using sets for efficient tracking
- Writing modular, reusable functions
- Input validation and clean console UI

## 👤 Author

**Jawad** | [GitHub](https://github.com/m145jawad-wq)

Built as Task 1 of the Datheon Python Programming Internship.
