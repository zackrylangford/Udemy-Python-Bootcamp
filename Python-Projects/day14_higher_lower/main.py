from art import *
from game_data import *
import random

#printing the logo
print(logo)

def get_random_choice(exclude=None):
    """Gets a random choice from data, excluding the provided entry if any."""
    pool = [d for d in data if d != exclude]
    return random.choice(pool)

#initial setup 
a = get_random_choice()
b = get_random_choice(a)
score = 0

def format_name(entry):
    """Takes the dictionary entry and returns the name, description, country, and follower count"""
    name = entry["name"]
    description = entry["description"]
    country = entry["country"]
    return f"{name}, {description}, from {country}"

def correct_answer(a, b):
    """Determines the correct answer for who has more followers and returns the value to be used to compare with user input"""
    a_count = a["follower_count"]
    b_count = b["follower_count"]
    if a_count > b_count:
        return "a"
    else:
        return "b"

# Main game function
def game(a, b, score):
    print(f"Choice A: " + format_name(a))
    print(vs)
    print(f"Choice B: " + format_name(b))
    answer = correct_answer(a,b)
    print(answer)
    a = b
    # Ask the user for their guess
    user_guess = input("Who has more followers? Type 'A' or 'B'\n").lower()

    if user_guess == answer:
        print("Correct!")
        score += 1
        print(f"Current score: {score}")
        b = get_random_choice(a)
        game(a, b, score)

    else: 
        print(f"Incorrect.\nFinal score: {score}")
        # End game


game(a, b, score)