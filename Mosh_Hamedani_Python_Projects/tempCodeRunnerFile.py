print("Welcome to the Number Guessing Game!")
random_number = random.randint(1, 100)
guess_count = 0
lives = 10

while True:
    try:
        if lives == 0:
            print(f"Game over! You've run out of lives. The number was {random_number}.")
            break

        guess = input("Guess the number (1-100) or 'q' to quit: ")
        if guess == 'q' or guess == 'Q':
            print(f"Thanks for playing! You made {guess_count} {'attempt' if guess_count == 1 else 'attempts'}!")
            break
        else:
            guess = int(guess)
            guess_count += 1
            lives -= 1
            if guess == random_number:
                print(f"Congrats! You guessed the number in {guess_count} {'attempt' if guess_count == 1 else 'attempts'}!")
                break
            elif guess < random_number:
                print(f"Too low! You have {lives} lives left.")
            else:
                print(f"Too high! You have {lives} lives left.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")
