class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("Hello my name is " + self.name)

    def wave(self):
        print("Waving hello")

p1 = Person("John", 36)

p1.say_hi()
p1.wave()

p2 = Person("Zack", 25)
p2.say_hi()
print(f"I am {p2.age} years old.")

quit = input("Press q to quit:")

while quit != "q":
    print("Try again")
    quit = input("Press q to quit:")

