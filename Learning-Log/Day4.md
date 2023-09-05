Day4 - Randomisation and Python Lists


*  Started with discussed randomisation and how python achieves this by creating a module for us to use. There is documentation on how to use the random function. 

Start by importing random at the top of a file

random.randint(0,100)

# You can use lots of different types of things from the random module, but the above is pretty basic. it will generate a random number between 0 and 100 (inclusive of both 0 and 100)

So, here is how to generate a coinflip:

import random
coin_flip = random.randint(0,1)
if coin_flip == 1:
    print("Heads")
else:
    print("Tails")


* We then discussed how to create our own modules in our python program. 

The key takeaway from this is that I learned that in order to call different things from my module you must import your module at the top of the file and then when you are working with it in the file you want to use the dot syntax by putting the module first and then what you want to use from the module. So: 

import my_module

my_module.myfunction

my_module.variable

* We didn't discuss this but you can also call classes and instances from classes from modules into the main file. Basically, anything that is a valid Python object can be called into the main file. 


Lists

* Square brackets with items seperated by a comma

fruits = ['banana', 'apple', 'pear']


We went over the basics of lists, talking about the index of the lists and why 0 is the first element of the list. 


talked about negative indices by using negative numbers to work from the end to the beginning. 

Talked about altering items from the list. 

fruits[0] = 'orange'

#That would change banana to orange in the original list. 




#To append to a list (added to the end) 


list.append('item')


# To extend a list with more than one item you can use extend() like so: 
list.extend(["item1", "item2"]) 

 
* We then worked with generating a random item from a list that we pulled through input, so we didn't know the total amount of items ahead of time. Here is a solution to it. The key is that we have to subtract 1 from the length of the list because if we don't, then the range that is used to generate the random number will actually be longer than the list itself, because of the starting index being 0. 

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
random_name = names[random.randint(0, len(names) - 1)]

print(f"{random_name} is going to buy the meal today!")


However, the best way to do it would be to use the choice() method instead. So: 

random_name = random.choice(names)


* We then did a nested list problem where we built a treasure map using nested lists, took input from a user and allowed them to place the x in a location within the nested list. So, the numbers were coordinates that indicated the column and row to place the "X"

* We then did a rock paper scissors game that combined everything

I need to work on tightening up my logic and thinking through all of the possibilities. I got the basic idea right, but there were a lot of ways I could have made it a lot simpler and also prepared for possible inputs outside of the range that I was checking for, so that I would avoid any possible errors. 
