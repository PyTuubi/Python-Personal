class Account():

    def __init__(self,owner,balance):

        self.owner = owner
        self.balance = balance

    def deposit(self,amount):

        self.balance = self.balance + amount
        print(f'Successfully added {amount}$ to account.')

    def withdraw(self,amount):

        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f'Successfully withdrew {amount}$ from account.')

        else:
            print("You don't have enough in your account.")

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: {self.balance}$'

myacc = Account('Jonni', 250)

print(myacc)

myacc.withdraw(250)

print(myacc)   

myacc.deposit(69)

print(myacc)
