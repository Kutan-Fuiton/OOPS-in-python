# Define a Employee class with attributes role, department and salary. This class also has a showDetails() method.
# Create an Engineer class that inherits from Employee and adds an additional attribute: name and age.


class Employee: 
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role:", self.role)
        print("Department:", self.dept)
        print("Salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

# e1 = Employee("Accountant", "Finance", "60,000")
# e1.showDetails()

engg1 = Engineer("Elon Musk", 40)
engg1.showDetails()