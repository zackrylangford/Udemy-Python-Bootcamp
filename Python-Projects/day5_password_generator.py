#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
password = ""

for amount in range(nr_letters):
    password += random.choice(letters)

for amount in range(nr_symbols):
    password += random.choice(symbols)

for amount in range(nr_numbers):
    password += random.choice(numbers)

# Convert the string to a list so we can shuffle it
password_list = list(password)

# Shuffle the list
random.shuffle(password_list)

# Convert the list back to a string
# This can be done as a for loop as well, but the following is much easier
# 
# For loop method:
# password = ''
# for char in password_list:
#    password += char

#Quick method
random_password = "".join(password_list)

print(f"Your secure randomized password is: {random_password}")
