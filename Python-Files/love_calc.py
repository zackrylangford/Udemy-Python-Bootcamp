# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_name1 = combined_names.lower()

t = lower_name1.count('t') 
r = lower_name1.count('r') 
u = lower_name1.count('u') 
e = lower_name1.count('e') 
l = lower_name1.count('l') 
o = lower_name1.count('o') 
v = lower_name1.count('v')

score = int((str(t+r+u+e)+str(l+o+v+e)))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else: 
    print(f"Your score is {score}.")


