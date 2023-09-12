from art import logo
import random
print(logo)

def play_game():  
    difficulty_levels = {"easy": 10, "hard": 5}
    
    while True:
        difficulty_level = input("What difficulty level would you like to play at? Easy or Hard\n").lower()
        if difficulty_level in difficulty_levels:
            guesses_remaining = difficulty_levels[difficulty_level]
            break
        else:
            print("Please select a valid difficulty.")

    cpu_choice = random.randint(1, 100)
    print("OK, I have selected a number. Try to guess it!")
    
    game_over = False

    while not game_over and guesses_remaining > 0: 
        try:
            guessed_number = int(input("Please guess a number between 1-100\n"))
        except ValueError:
            print("That's not a valid number.")
            continue
        
        guesses_remaining -= 1
        if guessed_number < cpu_choice:
            feedback = "Too low, guess again"
        elif guessed_number > cpu_choice:
            feedback = "Too high, guess again"
        else:
            feedback = "You got it!"
            game_over = True
        
        print(f"{feedback}\nGuesses remaining: {guesses_remaining}")

    play_again = input(f"You {'win' if game_over else 'lose'}!\nWould you like to play again? y or n\n")
    if play_again == "y":
        play_game()

play_game()
print("Thanks for playing, see you next time!")
