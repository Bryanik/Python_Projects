## Quiz Game

This is a simple quiz game implemented in Python. It asks the user a series of multiple-choice questions and provides feedback on whether the answers are correct or incorrect. At the end of the quiz, the user's score is displayed.

### Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Running the Quiz](#running-the-quiz)
- [Example](#example)

### Features
- Presents a series of multiple-choice questions to the user.
- Accepts user input for answers and checks if they are correct.
- Provides immediate feedback on the correctness of each answer.
- Displays the total score at the end of the quiz.

### Usage
1. Ensure you have Python installed on your system.
2. Copy the provided code into a Python file, for example, `quiz_game.py`.
3. Run the Python file to start the quiz.

### Code Explanation

#### Questions Data
The `questions` variable is a list of dictionaries, each representing a quiz question. Each dictionary contains:
- `prompt`: The question being asked.
- `options`: The multiple-choice options.
- `answer`: The correct answer.

#### Quiz Function
The `quiz()` function:
- Initializes the user's score to 0.
- Iterates over each question in the `questions` list.
- Prints the question and its options.
- Accepts user input for the answer.
- Checks if the answer is correct and updates the score.
- Provides feedback on the user's answer.
- Displays the total score at the end.

### Running the Quiz
To run the quiz, execute the Python script. You will be prompted to answer each question by typing in the corresponding letter (A, B, C, or D). After answering all questions, your total score will be displayed.

```python
questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    }
]

def quiz():
    score = 0

    for question in questions:
        print(question["prompt"])

        for option in question["options"]:
            print(option)

        answer = input("Enter your answer (A, B, C or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    
    print(f"You got {score} out of {len(questions)} questions correct.")

quiz()
```

### Example
When you run the script, it will display each question with its options, prompt you for an answer, and then display whether your answer was correct or not. At the end, it will show your total score.

```
What is the capital of France?
A. Paris
B. London
C. Berlin
D. Madrid
Enter your answer (A, B, C or D): A
Correct!

Which language is primarily spoken in Brazil?
A. Spanish
B. Portuguese
C. English
D. French
Enter your answer (A, B, C or D): B
Correct!

What is the smallest prime number?
A. 1
B. 2
C. 3
D. 5
Enter your answer (A, B, C or D): B
Correct!

Who wrote 'To Kill a Mockingbird'?
A. Harper Lee
B. Mark Twain
C. J.K. Rowling
D. Ernest Hemingway
Enter your answer (A, B, C or D): A
Correct!

You got 4 out of 4 questions correct.
```

This README provides an overview of the quiz game, including how to use it, a brief explanation of the code, and an example of what to expect when running the script.