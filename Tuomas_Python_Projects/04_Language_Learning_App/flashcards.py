import random

words = [
    {"spanish": "hola", "english": "hello"},
    {"spanish": "adiós", "english": "goodbye"},
    {"spanish": "gracias", "english": "thank you"},
    {"spanish": "por favor", "english": "please"},
    {"spanish": "lo siento", "english": "sorry"},
    {"spanish": "sí", "english": "yes"},
    {"spanish": "no", "english": "no"},
    {"spanish": "bien", "english": "good"},
    {"spanish": "mal", "english": "bad"},
    {"spanish": "hombre", "english": "man"},
    {"spanish": "mujer", "english": "woman"},
    {"spanish": "niño", "english": "boy"},
    {"spanish": "niña", "english": "girl"},
    {"spanish": "amigo", "english": "friend"},
    {"spanish": "familia", "english": "family"},
    {"spanish": "casa", "english": "house"},
    {"spanish": "escuela", "english": "school"},
    {"spanish": "comida", "english": "food"},
    {"spanish": "agua", "english": "water"},
    {"spanish": "perro", "english": "dog"},
    {"spanish": "gato", "english": "cat"},
    {"spanish": "día", "english": "day"},
    {"spanish": "noche", "english": "night"},
    {"spanish": "mañana", "english": "morning"},
    {"spanish": "tarde", "english": "afternoon"},
    {"spanish": "ayer", "english": "yesterday"},
    {"spanish": "hoy", "english": "today"},
    {"spanish": "mañana", "english": "tomorrow"},
    {"spanish": "libro", "english": "book"},
    {"spanish": "coche", "english": "car"}
]

def quiz_user(word_list):

    random.shuffle(word_list)
    score = 0

    for word in words: 
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
    
def main():
    print("Welcome to the Language Learning Flashcards App!\n")
    input("Press any key to start quiz...\n")
    quiz_user(words)

if __name__ == "__main__":
    main()
