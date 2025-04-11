#Static Methods: methods that dont use the self parameter (work at class level)

# def hello():
#     print("Hello")

# This method will show error because it dont have self parameter, but this function doesnt need self parameter, so for that we can make static methods

# @staticmethod
# def hello():
#     print("Hello")

# now this code will run, cuzz hello function been made a static function which works without self parameter

# @staticmethod --> this is also called decorators
# Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it. there are many more decorators other than static method.
# This static method decorators works like it takes a function and changes the behaviour of the function and give output as a function. here, the function is hello and the output is a function that can be called without self parameter. So we can use this decorator to make any function a static method.



class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    @staticmethod #decorators
    def hello():
        print("Hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, ", your average marks is:", sum/3)
        

s1 = Student("Tony Stark", [97, 88, 92])
s1.get_avg()
s1.hello()

