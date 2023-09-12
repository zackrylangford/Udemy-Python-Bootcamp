from art import logo
import random
print(logo)



# User asked what difficulty level and setting the original guesses_remaining variable
settings_chosen = False

while not settings_chosen:
    difficulty_level = input("What difficulty level would you like to play at? Easy or Hard\n").lower()
    if difficulty_level == "easy":
        guesses_remaining = 10
        settings_chosen = True
    elif difficulty_level == "hard":
        guesses_remaining = 5
        settings_chosen = True
    else:
        print("Please select a difficulty.")

#Computer chooses a random number between 1-100
cpu_choice = random.choice(range(101))

#Debug statement - To be removed
print(f"User guesses remaining: {guesses_remaining}")

#Debug statement - To be removed
print(f"CPU number chosen: {cpu_choice}")

game_over = False

while not game_over: 
    guessed_number = int(input("Please guess a number between 1-100\n"))
    print(f"You guessed: {guessed_number}")

      