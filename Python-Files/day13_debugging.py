############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(21):
#     if i == 20:
#       print("You got it")
# my_function()

# Nothing happens because the range that is inputted is 1-19, not 1-20. The if statement is never true.

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5) #The original had 1, 6 which caused an index error because the list starts counting at 0. This also omitted the first item in the list. To fix it we use the range 0, 5 which includes the first item in the list and cuts off before going beyond the last item in the list.
# print(dice_imgs[dice_num])


# # Play Computer
# year = int(input("What's your year of birth?"))
# if year >= 1980 and year <= 1994: # The original had the year > 1980 and year < 1994 which caused the millenial print statement to never be true. To fix it we use the >= and <= operators.
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# # The original had an == operator which made it not assign the user input into the word_per_page variable, so it was never updated. Using a print statement revealed that it was not getting updated, so that leads us to focus on the word_per_page variable and how it is being updated. To fix it we use the = operator to assign the user input into the word_per_page variable
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])