# Create a class called Order which stores item and its price.
# Use Dunder function __gt__() to convey that:
# order1 > order 2 if price of order1 > price of order2.

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):
        return self.price > other.price
    
odr1 = Order("Chips", 20)
odr2 = Order("Chips", 15)

print(odr1 > odr2) # True
print(odr2 > odr1) # False



# __gt__ is a dunder function which is used to overload the > operator.
# So here we are using the __gt__ function to compare the price of two orders.