from User import User

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
    
    def deposit(self,amount):
        self.amount = amount
        self.balance= self.balance + self.amount

        print("Account Balance has been updated : "+"Rs."+ str( self.balance )+ " only")

    def withdraw(self,amount1):
        self.amount1 = amount1
        if self.amount1 > self.balance:
            print("Insufficient Funds: Balance available: " + "Rs." + str(self.balance)+ ".00"+ " only")
        else:
            self.balance = self.balance - self.amount1
            print("Account balance has been updated: " + "Rs." + str(self.balance) +".00"+ " only")
    
    def view_balance(self):
        self.show_details()
        print("Account Balance has been updated: " + "Rs." +str(self.balance)+".00" + " only")

    
Hari = Bank('Hari',21,'Female')
Hari.show_details()
Hari.deposit(1000)
Hari.withdraw(1800)
Hari.view_balance()


