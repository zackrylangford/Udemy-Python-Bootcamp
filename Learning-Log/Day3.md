Day 3 - Controlling flow and logical operators

This was all about using the if statement and comparisons in order to do calculations and comparisons. We talked about how to control flow using flow charts and how it is a good idea to set up a flow chart before writing out code so that you can know exactly what you are trying to do. 

so you can use things like: 

if x == "y": 
    #then do something
elif x == "z":
    #then do something
else: 
    #anything else that x is will be executed here

The key takeaway from this for me is that once a condition is met and the code executes, then the rest of the statements will be ignored, so they won't be checked. 

* We talked about nested if statements, so you can check multiple conditions

if year % 2 == 0:
    if year % 100 == 0: 
	#And so on

We did the leap year challenge, where you have to code something that can determine whether or not a given year is a leap year. Here is the example: 



year = input("Provide a year and I will check if it is a leap year\n ('q' to quit)")

while year != "q":
   
    if int(year) % 4 == 0:
        if int(year) % 100 == 0:
            if int(year) % 400 == 0:
                print("Leap year")
            else:
                print("Not leap year")
        else:
            print("Leap year")
    else:
        print("Not leap year")
    year = input("Provide a year and I will check if it is a leap year\n ('q' to quit)")


* We also worked on multiple if statements in a row, like if x > 3 and x < 10:, which checks x against multiple conditions at once.

* We did a love calculator that checked how many times letters occured in a string, using the count() function. You can specify a variable and provide an argument to check and see if something is present in the string like: 

string1.count("x") 


This will count how many times x is found in string1 

* We also discussed the built in lower(), upper(), uppercase(), lowercase() functions and what they do. 

* We built a simple adventure game that walked a user through different choices and based on what they chose we moved them through different scenarios. 




