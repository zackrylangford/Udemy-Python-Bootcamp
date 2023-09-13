number = int(input("Which number do you want to check?"))

if number % 2 == 0:
  # The original had only a single = operator which caused a syntax error. To fix it we use the == operator.
  print("This is an even number.")
else:
  print("This is an odd number.")
  
