# There are basically four pillars of OOPS:
# 1. Abstraction
# 2. Encapsulation
# 3. Inheritance
# 4. Polymorphism


# Abstraction --> Hiding the implementation details of a class and only showing the essential features to the user. just avoid showing unnecessary things, only shows necessary things.

# For example:- 

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car started..")
# car1 = Car()
# car1.start() # Car started..

# Now here what's happening is that we are hiding the implementation details of the class Car. We are not showing how the car is started, we are just showing that the car is started. So this is abstraction.



# Encapsulation --> Wrapping data and functions into a single unit (object)