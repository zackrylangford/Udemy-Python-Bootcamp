from art import logo
import random
print(logo)

def play_game():  
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
    cpu_choice = random.choice(range(1, 101))

    print("OK, I have selected a number. Try to guess it!")

    game_over = False

    while not game_over and guesses_remaining > 0: 
        try:
            guessed_number = int(input("Please guess a number between 1-100\n"))
        except ValueError:
            print("That's not a valid number.")
            continue
        if guessed_number < cpu_choice:
            print("Too low, guess again")
            guesses_remaining -= 1
            print(f"Guesses remaining: {guesses_remaining}")
        elif guessed_number > cpu_choice:
            print("Too high, guess again")
            guesses_remaining -= 1
            print(f"Guesses remaining: {guesses_remaining}")
        elif guessed_number == cpu_choice:
            print("You got it!")
            game_over = True

    if guesses_remaining == 0 and game_over == False:
        play_again = input("You lose, sorry!\nWould you like to play again? y or n\n")
        if play_again == "y":
            play_game()
    elif guesses_remaining >= 0 and game_over == True:
        play_again = input("You win!\nWould you like to play again? y or n\n")
        if play_again == "y":
            play_game()


play_game()

print("Thanks for playing, see you next time!")