from art import *
from game_data import *
import random


ANSWER = ""

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
    a_count = a["follower_count"]
    b_count = b["follower_count"]
    if a_count > b_count:
        return "a"
    else:
        return "b"

def continue_game():
    pass

# Main game function
def game():
    #Inital game setup 
    a = random.choice(data)
    b = random.choice(data)
    print(f"Choice A: " + format_name(a))
    print(vs)
    print(f"Choice B: " + format_name(b))

    answer = correct_answer(a,b)
    print(f"Correct Answer hint: " + answer)
    if answer == "b":
        a = b

    # Ask the user for their guess
    user_guess = input("Who has more followers? Type 'A' or 'B'\n").lower()

    if user_guess == answer:
        print("Correct!")
        game()

    else: 
        print("Incorrect.")
        # End game


game()