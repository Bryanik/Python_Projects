# Language Learning Flashcards App

Welcome to the Language Learning Flashcards App! This simple command-line application helps users practice their Spanish-to-English vocabulary through a quiz format. 

## Features

- Randomized flashcards to test your Spanish vocabulary knowledge.
- Immediate feedback on whether the user's answer is correct or not.
- Tracks the user's score throughout the quiz.
- Allows the user to quit the quiz at any time by entering 'Q'.

## Installation

1. Ensure you have Python installed on your system.
2. Download or clone this repository to your local machine.

## Usage

1. Navigate to the directory containing the script.
2. Run the script using Python:

   ```bash
   python flashcards.py
   ```

3. Follow the on-screen instructions to start the quiz and answer each question.

## Code Overview

The main components of the code include:

1. **Data Structure**: A list of dictionaries where each dictionary contains a Spanish word and its English translation.

   ```python
   words = [
       {"spanish": "hola", "english": "hello"},
       {"spanish": "adiós", "english": "goodbye"},
       ...
   ]
   ```

2. **Quiz Function**: This function shuffles the list of words, prompts the user for the English translation of each Spanish word, checks the user's answer, and updates the score.

   ```python
   def quiz_user(word_list):
       random.shuffle(word_list)
       score = 0

       for word in word_list:
           print(f"What is the English translation of '{word['spanish']}'?\n")
           user_answer = input("Enter your answer or 'Q' to quit: ").strip().lower()
           correct_answer = word['english'].lower()

           if user_answer == correct_answer:
               score += 1
               print("Correct!\n")
           elif user_answer == "q":
               break
           else:
               print(f"Wrong! The correct answer is '{word['english']}'.\n")
               
       print(f"Quiz ended! Your score is {score}/{len(word_list)}")
   ```

3. **Main Function**: This function welcomes the user and starts the quiz.

   ```python
   def main():
       print("Welcome to the Language Learning Flashcards App!\n")
       input("Press any key to start quiz...\n")
       quiz_user(words)

   if __name__ == "__main__":
       main()
   ```

## Example

Upon running the script, the user will see the following prompt:

```plaintext
Welcome to the Language Learning Flashcards App!

Press any key to start quiz...

What is the English translation of 'hola'?
Enter your answer or 'Q' to quit: hello
Correct!

What is the English translation of 'adiós'?
Enter your answer or 'Q' to quit: goodbye
Correct!

...

Quiz ended! Your score is 2/2
```

Happy coding :)