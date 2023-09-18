Day 2 Learning Log - We focused on data types and created a BMI calculator. So, it was a lot of learning how to manipulate different data types. 

1. You can use int or float for numbers. Integers are whole numbers, float is decimals. 

Int - good for tracking whole numbers like users in an app or items in an inventory

Float - good  

You can change the type by using different built in functions like int(number) or float(number) or if you want to change it into a string you can use str(number), which will turn the number into a string. 


2. You can use the built in round() function to round your floats to the nearest whole number. 

so, round(2.34)

or if you are using a variable

number1 = 2.344324

print(round(number1))

Output: 2

You can specify the number of decimal points by adding a second argument. 

x = 5.6789
rounded_x = round(x, 2)  # Rounds to 2 decimal places
print(rounded_x)  # Output will be 5.68



You can use string formatting to control the number of decimal places as well: 

x = 5.6789
formatted_x = "{:.2f}".format(x)  # Formats to 2 decimal places
print(formatted_x)  # Output will be "5.68"


3. We discussed mathematical operations in Python as well, going over how you can do calculations


4. We discussed f strings for printing variables out instead of doing concatenation. This allows direct insertion of the variables without having to manipulate the data type at all. 

message = "go to school please" 

name = "Zack"

print(f"{message}, {name}")

Output: go to school please, Zack


5. We also built a tip calculator that did a lot of calculations and had to change the data types in order to output stuff. 

