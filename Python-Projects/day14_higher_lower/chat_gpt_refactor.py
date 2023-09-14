from art import *
from game_data import *
import random

print(logo)

def get_random_choice(exclude=None):
    """Gets a random choice from data, excluding the provided entry if any."""
    pool = [d for d in data if d != exclude]
    return random.choice(pool)

a = get_random_choice()
b = get_random_choice(a)

def format_name(entry):
    """Takes the dictionary entry and returns the formatted string."""
    return f'{entry["name"]}, {entry["description"]}, from {entry["country"]}'

def get_correct_answer(a, b):
    """Determines the correct answer for who has more followers."""
    return "a" if a["follower_count"] > b["follower_count"] else "b"

def game(a, b):
    print(f"Choice A: {format_name(a)}")
    print(vs)
    print(f"Choice B: {format_name(b)}")
    
    answer = get_correct_answer(a, b)
    a = b
    
    user_guess = input("Who has more followers? Type 'A' or 'B'\n").lower()

    if user_guess == answer:
        print("Correct!")
        b = get_random_choice(a)
        game(a, b)
    else: 
        print("Incorrect.")

game(a, b)
