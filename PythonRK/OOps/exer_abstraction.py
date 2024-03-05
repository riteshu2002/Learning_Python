class Account:
    def __init__(self,bal,acc) -> None:
        self.balance = bal
        self.account_no = acc 

    # Debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs ",amount, "was debitted")

    def credit(self,amount):
        self.balance += amount
        print("Rs ",amount, "was creditted")
    
    def get_bal(self):
        return self.balance
    

acc1 = Account(1000,1233445)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(200)
acc1.credit(3000)
print("Balance Enquiry: ".acc1.get_bal())