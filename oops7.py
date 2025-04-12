# class method:- class method is bound to the class and receives the class as an implicit first argument. Note- static method can't access or modify class state and generally for utility.

# Syntax:- 

# class Student:
#     @classmethod
#     def college( cls ):
#         pass
# For example:-


# 1. 
# class Person: 
#     name = "anonymous"
    
#     def changeName(self, name):
#         self.name = name

# p1 = Person()
# p1.changeName("Rahul Kumar")
# print(p1.name) # prints Rahul Kumar
# print(Person.name) # prints anonymous


# 2. 
# class Person: 
#     name = "anonymous"
    
#     def changeName(self, name):
#         Person.name = name

# p1 = Person()
# p1.changeName("Rahul Kumar")
# print(p1.name) # prints Rahul Kumar
# print(Person.name) # prints Rahul Kumar


# 3. 
# class Person: 
#     name = "anonymous"
    
#     def changeName(self, name):
#         self.__class__.name = name

# p1 = Person()
# p1.changeName("Rahul Kumar")
# print(p1.name) # prints Rahul Kumar
# print(Person.name) # prints Rahul Kumar


# 4. 
class Person: 
    name = "anonymous"
    
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Rahul Kumar")
print(p1.name) # prints Rahul Kumar
print(Person.name) # prints Rahul Kumar




# So still now we explored three methods:-
# 1. static method - when class and instance both are not required to be passed as an implicit first argument.
# 2. instance method ( self ) - when instance is required to be passed as an implicit first argument.
# 3. class method ( cls ) - when class is required to be passed as an implicit first argument.