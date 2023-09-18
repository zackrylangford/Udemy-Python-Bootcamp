# Object Oriented Programming

## Difference between Procedural and Object Oriented Programming

### Procedural Programming

- Procedural programming is about writing procedures or functions that perform operations on the data, while Object-oriented programming is about creating objects that contain both data and functions.

- Procedural programming follows top down approach. In procedural programming, program is divided into subroutines or functions. In object-oriented programming, program is divided into objects.

- Procedural programming does not have any proper way for hiding data so it is less secure. While object-oriented programming provides data hiding so it is more secure.

### Object Oriented Programming

- Object-oriented programming follows bottom up approach in program design. In object-oriented programming, program is divided into objects.

- Object-oriented programming provides data hiding so it is more secure. While procedural programming does not provide data hiding so it is less secure.

- Object-oriented programming provides ability to simulate real-world event much more effectively. While procedural programming does not provide such feature.

- Object-oriented programming makes development and maintenance easier where as in procedural programming it is not easy to manage if code grows as project size grows.

### How to use OOP in Python

Example: A waiter at a restaurant is an object. The customer is an object. The menu is an object. The chef is an object. The table is an object. The bill is an object. The restaurant is an object.

The Waiter has two things. It has attributes and it has methods. The attributes are the things that the waiter has. The methods are the things that the waiter can do.

The Waiter has a name, an age, a height, a hair color, a uniform, a salary, a tip, a table number, a menu, a bill, a customer, a chef, a restaurant, a shift, a section, etc. 

Example code:
    
```python

    class Waiter:
        ##These are things that the waiter has
        def __init__(self, name, age, height, hair_color, uniform, salary, tip, table_number, menu, bill, customer, chef, restaurant, shift, section):
            self.name = name
            self.age = age
            self.height = height
            self.hair_color = hair_color
            self.uniform = uniform
            self.salary = salary
            self.tip = tip
            self.table_number = table_number
            self.menu = menu
            self.bill = bill
            self.customer = customer
            self.chef = chef
            self.restaurant = restaurant
            self.shift = shift
            self.section = section

        ##These are things that the waiter can do
        def greet_customer(self):
            print(f"Hello, my name is {self.name} and I will be your waiter today. What can I get you to drink?")

        def take_order(self):
            print(f"Okay, I will get you a {self.menu} and a {self.menu}.")

        def bring_food(self):
            print(f"Here is your {self.menu} and your {self.menu}. Enjoy your meal!")

        def bring_bill(self):
            print(f"Here is your bill. Your total is {self.bill}.")

        def take_payment(self):
            print(f"Thank you for dining with us today. Your total is {self.bill}. Your tip is {self.tip}. Have a great day!")

        def clean_table(self):
            print(f"Table {self.table_number} has been cleaned and is ready for the next customer.")

        def clock_out(self):
            print(f"Thank you for working today. Your shift is over. You worked {self.shift} hours today. Have a great day!")

        def seat_customer(self):
            print(f"Welcome to {self.restaurant}. My name is {self.name} and I will be your waiter today. Please follow me to your table in section {self.section}.")

        def take_break(self):
            print(f"Thank you for working so hard. You can take a break now. You have worked {self.shift} hours today. Have a great day!")

        def clock_in(self):
            print(f"Welcome to work today. Your shift is starting now. You will be working in section {self.section} today. Have a great day!")

        def take_order(self):
            print(f"Okay, I will get you a {self.menu} and a {self.menu}.")

```

### Classes are like blueprints

- Classes are like blueprints. They are the blueprint for an object. They tell the computer what the object is and what it can do.

- Classes are like a cookie cutter. They are the cookie cutter for an object. They tell the computer what the object is and what it can do.

### Objects are like cookies

- Objects are like cookies. They are the cookie that is made from the cookie cutter. They are the thing that is made from the blueprint.


### How to create a class

* PascalCase for class names - every word starts with a capital letter
