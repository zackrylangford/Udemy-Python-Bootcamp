height = int(input("How tall are you?"))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you?"))
    if age < 12:
        bill = 5
    elif age <=18:
        bill = 7
    elif age > 18:
        if age >=45 and age <=55:
            print("Your ticket is free, hope you feel better soon!")
            bill = 0
        else:
            bill = 12
            print("Adult tickets are $12")
    
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill+=3

    print(f"Your total ticket costs ${bill}")

else:
    print("You cannot ride the rollercoaster")