# Polymorphism : Operator Overloading --> When the same operator is allowed to have different meaning according to the context.

#For Example:- 
# print(2+3) # adding
# print(type(1)) # class int

# print("2"+"3") # concatenation
# print(type("2")) # class str

# print([2,3]+[4,5]) # merging
# print(type([2, 3])) # class list

# operator overloading is a way to give new meaning to the existing operator.



class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    # This is normal function
    # def add(self, num2):
    #     newReal = self.real + num2.real
    #     newImg = self.img + num2.img
    #     return Complex(newReal, newImg)

    # This is dunder function
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)




num1 = Complex(1, 3)
num1.showNumber() # prints 1 i + 3 j

num2 = Complex(4, 6)
num2.showNumber() # prints 4 i + 6 j


# what if we want to add two complex numbers using + operator? simple like num3 = num1 + num2, instead of using num3 = num1.add(num2)
# we can do this by overloading the + operator.
# by using dunder functions, we can overload the + operator.

# num3 = num1.add(num2) # num3 = num1 + num2
# num3.showNumber() # prints 5 i + 9 j

num3 = num1 + num2 #Here we used the dunder function
num3.showNumber() # prints 5 i + 9 j

num3 = num1 - num2 #Here we used the dunder function
num3.showNumber() # prints -3 i + -3 j














