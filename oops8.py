# Property decorator:- we use @property decorator on any method in the class to use the method as a property
#  For example:-


# 1. Normally

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math= math
#         self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

# stu1 = Student(98, 97, 99)
# print(stu1.percentage) # prints 98.0%

# # Imagine a case where there is rechecking error and have to update a marks of one subject.
# stu1.phy = 86
# print(stu1.phy)
# print(stu1.percentage) # prints 98.0% --> Here the percentage is not updated as we are not using @property decorator. So we need to use @property decorator to update the percentage when the marks are updated.




# 2. we can make a percentage calculate method for this

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math= math
#         self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

#     def calcPercentage(self):
#         self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

# stu1 = Student(98, 97, 99)
# print(stu1.percentage) # prints 98.0%


# stu1.phy = 86
# print(stu1.phy)
# stu1.calcPercentage() # print 94.0%
# print(stu1.percentage) 



# 3. But this is not a good way to do this. So we can use @property decorator to make it a property.

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math= math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage) # prints 98.0%


stu1.phy = 86
print(stu1.percentage) # prints 94.0% 



# So now we can use the method as a property and it will automatically update the value when the value of the instance variable is updated. After making the method as a property, the attribute inside that method like self.phy, self.chem and self.math will be used as a property and it will automatically update the value when the value of the instance variable is updated. So we can use @property decorator to make a method as a property.