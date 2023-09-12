from art import logo

print(logo)

# User asked what difficulty level and setting the original guesses_remaining variable

difficulty_level = input("What difficulty level would you like to play at? Easy or Hard\n").lower()

if difficulty_level == "easy":
    guesses_remaining = 10
elif difficulty_level == "hard":
    guesses_remaining = 5

print(guesses_remaining)
