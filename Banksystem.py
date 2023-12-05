#parent class
class User:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender =gender

    def show_user_details(self):
        print("\nPERSON DETAILS")
        print("*****************************")
        print("\nName: ",self.name)
        print("Age: ", self.age)
        print("Gender: ",self.gender)
        print("\n*****************************")

#p1  = User("Rohan",19,"Male")
#p1.show_user_details()

#child class

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0
        
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance +amount
        print("\nThe amount deposited: ",amount)
        print("Account balance has been updated: ",self.balance)

    def withdraw(self,amount):
        self.amount = amount

        if self.balance < self.amount:
            print("\ninsufficient funds | balance available: ",self.balance)
        else:
            self.balance = self.balance - self.amount
            print("\nThe amount withdrawed: ",amount)
            print("Account balance has been updated: ",self.balance)

    def view_balance(self):
        print("\n*******************************")
        print("\nThe balance available is ",self.balance)
    

b1 = Bank("Akash",23,"male")
b1.show_user_details()

b1.deposit(100)
b1.deposit(20)
b1.withdraw(35)

b1.view_balance()
