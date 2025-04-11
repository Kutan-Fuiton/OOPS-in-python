# Create student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, ", your average marks is:", sum/3)
        

s1 = Student("Tony Stark", [97, 88, 92])
s1.get_avg()

s1.name="Iron Man" #changing the name of the student later also could change the name 
s1.get_avg()