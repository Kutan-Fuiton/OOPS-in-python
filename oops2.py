# Methods: there are init functions with that we can create different methods. like here welcome funciton and get_marks function


class Student:
    college_name="ABC College"

    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks 
        print("adding new student in Database..")

    def welcome(self):
        print("welcome student,",self.name)

    def get_marks(self):
        return self.marks

s1 = Student("karan",97)
s1.welcome() 
print(s1.get_marks()) 