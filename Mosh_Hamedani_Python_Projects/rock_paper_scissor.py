import random
import sys

def dontPlayAgain():
    print(f"Thanks for playing, {name}! You scored {score[name]} points and the computer scored {score['computer']} points.")
    sys.exit()

def retryPlayAgain():
    while True:
        print("Invalid choice. Please enter y or n.")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == "n" or play_again == "no":
            dontPlayAgain()
        elif play_again == "y" or play_again == "yes":
            print("Let's play again!")
            break
        else:
            continue

print("Welcome to Rock, Paper, Scissors!")
name = input("What is your name? ")
print(f"Nice to meet you, {name}! Let's play Rock, Paper, Scissors!")
score = {name: 0, "computer": 0}

while True:
    user_choice = input("Enter your choice (r/p/s): ").lower()
    if user_choice not in ["r", "p", "s", "rock", "paper", "scissors"]:
        print("Invalid choice. Please enter r, p, or s.")
        continue
    elif user_choice == "r" or user_choice == "rock":
        user_choice = "🪨"
    elif user_choice == "p" or user_choice == "paper":
        user_choice = "📃"
    elif user_choice == "s" or user_choice == "scissors":
        user_choice = "✂️"

    computer_choice = random.choice(["🪨", "📃", "✂️"])
    print(f"You chose {user_choice}  and the computer chose {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "🪨" and computer_choice == "✂️":
        print("You win!")
        score[name] += 1
    elif user_choice == "📃" and computer_choice == "🪨":
        print("You win!")
        score[name] += 1
    elif user_choice == "✂️" and computer_choice == "📃":
        print("You win!")
        score[name] += 1
    else:
        print("You lose!")
        score["computer"] += 1

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "n" or play_again == "no":
        dontPlayAgain()
    elif play_again == "y" or play_again == "yes":
        continue
    else:
        retryPlayAgain()
