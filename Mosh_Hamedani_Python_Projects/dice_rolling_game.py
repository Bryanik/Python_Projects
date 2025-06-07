import random

def roll_dice(num_dice):
    if num_dice > 10:
        print("Error: Cannot roll more than 10 dice at once!")
        return None
    elif num_dice < 1:
        print("Error: Must roll at least 1 die!")
        return None
    
    dice_results = [random.randint(1, 6) for _ in range(num_dice)]
    return dice_results

games_played = 0
while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y" or choice == "yes":
        try:
            num_dice = int(input("How many dice would you like to roll? (1-10): "))
            result = roll_dice(num_dice)
            if result is not None:
                print(f"You rolled: {', '.join(map(str, result))}")
                games_played += 1
        except ValueError:
            print("Please enter a valid number!")
        except Exception as e:
            print(f"An error occurred: {e}")
    elif choice == "n" or choice == "no":
        print(f"\nThanks for playing! You played {games_played} {'time' if games_played <= 2 else 'times'}.")
        break
    else:
        print("Invalid choice!")
