import random

words = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift']
chosenWord = random.choice(words)
wordDisplay = ['_' for _ in chosenWord]
attempts = 5

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

if "_" not in wordDisplay:
    print("Congratulations! You guessed the right word.")
    print("".join(wordDisplay))
    print("You won!")
else:
    print("You have 0 attempts left!")
    print("The right word was: " + chosenWord)
    print("You failed!")