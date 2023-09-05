rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player_choice = int(input("Choose 1, 2, or 3. Rock = 1, Paper = 2, Scissors = 3\n\n"))
computer_choice = random.randint(1,3)

if player_choice == 1:
    print(f"Player Choice: Rock\n{rock}")
elif player_choice == 2:
    print(f"Player Choice: Paper\n{paper}")
elif player_choice == 3:
    print(f"Player Choice: Scissors\n{scissors}")

if computer_choice == 1:
    print(f"Computer Choice: Rock\n{rock}")
elif computer_choice == 2:
    print(f"Computer Choice: Paper\n{paper}")
elif computer_choice == 3:
    print(f"Computer Choice: Scissors\n{scissors}")

if player_choice == computer_choice:
    print("Draw")
elif player_choice == 1 and computer_choice == 3:
    print("Player wins!")
elif player_choice == 2 and computer_choice == 1:
    print("Player wins!")
elif player_choice == 3 and computer_choice == 2:
    print("Player wins!")

elif player_choice == 1 and computer_choice == 2:
    print("Computer wins!")

elif player_choice == 2 and computer_choice == 3:
    print("Computer wins!")

elif player_choice == 3 and computer_choice == 1:
    print("Computer wins!")


import random

# Create a dictionary to store the choices and their corresponding ASCII art
choices = {
    1: ("Rock", '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''),
    2: ("Paper", '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''),
    3: ("Scissors", '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')
}

player_choice = int(input("Choose 1, 2, or 3. Rock = 1, Paper = 2, Scissors = 3\n\n"))
computer_choice = random.randint(1, 3)

# Display player and computer choices
print(f"Player Choice: {choices[player_choice][0]}\n{choices[player_choice][1]}")
print(f"Computer Choice: {choices[computer_choice][0]}\n{choices[computer_choice][1]}")

# Determine winner
if player_choice == computer_choice:
    print("Draw")
elif (player_choice - computer_choice) % 3 == 1:
    print("Player wins!")
else:
    print("Computer wins!")



# HEre is the best way to do it: 

game_images = [rock, paper, scissors]

print(game_images[player_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if player_choice >= 3 or player_choice < 0: 
    print("You typed an invalid number, you lose")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and player_choice == 2:
    print("You lose")
elif computer_choice > player_choice:
    print("You lose!")
elif player_choice > computer_choice:
    print("You win!")
elif computer_choice == player_choice:
    print("Draw")
