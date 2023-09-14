from art import *
from game_data import *
import random

#printing the logo
print(logo)

def format_name(entry):
    """Takes the dictionary entry and returns the name, description, country, and follower count"""
    name = entry["name"]
    description = entry["description"]
    country = entry["country"]
    return f"{name}, {description}, from {country}"

def correct_answer(a, b):
    """Determines the correct answer for who has more followers and returns the value to be used to compare with user input"""
    a_name = a["name"]
    b_name = b["name"]
    a_count = a["follower_count"]
    b_count = b["follower_count"]
    print(a_count)
    print(b_count)
    return f"{a_name} has {a_count} and {b_name} has {b_count}"


# Main game function
def game():
    #Inital game setup 
    a = random.choice(data)
    b = random.choice(data)
    choice_a = format_name(a)
    choice_b = format_name(b)
    print(f"Choice A: {choice_a}")
    print(vs)
    print(f"Choice B: {choice_b}")

    print(correct_answer(a, b))

    # Ask the user for their guess
    user_guess = input("Who has more followers? Type 'A' or 'B'\n")



game()