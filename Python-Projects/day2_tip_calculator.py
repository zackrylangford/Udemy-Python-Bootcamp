#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!\n")

total_bill = float(input("What was the total bill?\n"))  # Changed to float to accept decimal input

tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))

split_number = int(input("How many people to split the bill?\n"))

total_calc = (total_bill / split_number)

amount = (total_bill / split_number) * ((tip_percent / 100) + 1)

print(f"Each person should pay: ${amount:.2f}")  