# Create Account class wiht 2 attributes - balance & account number. Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    #debit method    
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    #credit method    
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())

    #check balance method    
    def get_balance(self):
        return self.balance

acc1 = Account(10000, 1234567890)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)