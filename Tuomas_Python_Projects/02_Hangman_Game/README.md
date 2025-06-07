## Hangman Game

This is a simple command-line Hangman game implemented in Python. The game randomly selects a word from a predefined list, and the player attempts to guess the word by suggesting letters. The player has a limited number of attempts to guess the word correctly.

### Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Running the Game](#running-the-game)
- [Example](#example)

### Features
- Randomly selects a word from a predefined list.
- Displays the word with underscores representing unguessed letters.
- Accepts user input for guessing letters.
- Provides feedback on whether the guessed letter is in the word.
- Limits the number of incorrect guesses to 5.
- Displays the word and the outcome (win or lose) at the end of the game.

### Usage
1. Ensure you have Python installed on your system.
2. Copy the provided code into a Python file, for example, `hangman_game.py`.
3. Run the Python file to start the game.

### Code Explanation

#### Importing the Random Module
```python
import random
```
The `random` module is imported to randomly select a word from the list of words.

#### Defining the List of Words and Choosing a Random Word
```python
words = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift']
chosenWord = random.choice(words)
```
- `words`: A list of words that the game will randomly choose from.
- `chosenWord`: The word randomly selected from the `words` list.

#### Initializing the Display and Attempts
```python
wordDisplay = ['_' for _ in chosenWord]
attempts = 5
```
- `wordDisplay`: A list of underscores representing the unguessed letters of the chosen word.
- `attempts`: The number of incorrect guesses the player is allowed.

#### Main Game Loop
```python
while '_' in wordDisplay and attempts > 0:
    print("\n" + " ".join(wordDisplay))
    guess = input("Enter a missing letter: ")

    if guess in chosenWord:
        for index, letter in enumerate(chosenWord):
            if letter == guess:
                wordDisplay[index] = letter
    else:
        print("You didn't guess a missing letter.")
        attempts -= 1
```
- The game continues as long as there are unguessed letters and the player has remaining attempts.
- The current state of the word is displayed.
- The player is prompted to guess a letter.
- If the guessed letter is in the chosen word, the display is updated.
- If the guessed letter is not in the chosen word, the number of attempts is decreased.

#### End of Game
```python
if "_" not in wordDisplay:
    print("Congratulations! You guessed the right word.")
    print("".join(wordDisplay))
    print("You won!")
else:
    print("You have 0 attempts left!")
    print("The right word was: " + chosenWord)
    print("You failed!")
```
- If the player successfully guesses the word, a congratulatory message is displayed.
- If the player runs out of attempts, the correct word is revealed and a failure message is displayed.

### Running the Game
To run the game, execute the Python script. You will be prompted to enter missing letters until you either guess the word correctly or run out of attempts.

```sh
python hangman_game.py
```

### Example
When you run the script, it will display the word as underscores, prompt you for letters, and provide feedback. Here is an example interaction:

```
_ _ _ _ _ _

Enter a missing letter: p
p _ _ _ _ _

Enter a missing letter: y
p y _ _ _ _

Enter a missing letter: t
p y t _ _ _

Enter a missing letter: h
p y t h _ _

Enter a missing letter: o
p y t h o _

Enter a missing letter: n
p y t h o n

Congratulations! You guessed the right word.
python
You won!
```

This README provides an overview of the Hangman game, including how to use it, a brief explanation of the code, and an example of what to expect when running the script.