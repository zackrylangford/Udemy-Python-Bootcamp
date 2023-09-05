


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
