import random
import json
from datetime import datetime
from pathlib import Path

def load_high_scores():
    high_scores_file = Path("high_scores.json")
    if high_scores_file.exists():
        with open(high_scores_file, "r") as f:
            return json.load(f)
    return {"easy": None, "medium": None, "hard": None}

def save_high_score(difficulty, attempts, current_score):
    high_scores = load_high_scores()
    score_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # If no previous score or new score is better
    if (high_scores[difficulty] is None or 
        attempts < high_scores[difficulty]["attempts"]):
        high_scores[difficulty] = {
            "attempts": attempts,
            "date_time": score_time
        }
        with open("high_scores.json", "w") as f:
            json.dump(high_scores, f, indent=4)
        return True
    return False

def display_high_score(difficulty):
    high_scores = load_high_scores()
    score = high_scores[difficulty]
    if score:
        print(f"\nHigh Score for {difficulty.capitalize()} Mode:")
        print(f"Attempts: {score['attempts']}")
        print(f"Achieved on: {score['date_time']}")
    else:
        print(f"\nNo high score yet for {difficulty.capitalize()} mode!")

print("Welcome to the Number Guessing Game!")
difficulty = input("Choose the difficulty level (easy, medium, hard): ").lower()

match difficulty:
    case "easy":
        random_number = random.randint(1, 10)
    case "medium":
        random_number = random.randint(1, 100)
    case "hard":
        random_number = random.randint(1, 1000)
    case _:
        print("Invalid difficulty level. Please choose 'easy', 'medium', or 'hard'.")
        exit()

guess_count = 0
lives = 10
game_won = False

while True:
    try:
        if lives == 0:
            print(f"Game over! You've run out of lives. The number was {random_number}.")
            break

        guess = input(f"Guess the number between 1 and {'10' if difficulty == 'easy' else '100' if difficulty == 'medium' else '1000'} or 'q' to quit: ")

        if guess.lower() == 'q':
            print(f"Thanks for playing! You made {guess_count} {'attempt' if guess_count == 1 else 'attempts'}!")
            break
        else:
            guess = int(guess)
            guess_count += 1
            lives -= 1
            if guess == random_number:
                game_won = True
                print(f"Congrats! You guessed the number in {guess_count} {'attempt' if guess_count == 1 else 'attempts'}!")
                if save_high_score(difficulty, guess_count, None):
                    print("🎉 New High Score! 🎉")
                display_high_score(difficulty)
                break
            elif guess < random_number:
                print(f"Too low! You have {lives} lives left.")
            else:
                print(f"Too high! You have {lives} lives left.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if not game_won:
    display_high_score(difficulty)
