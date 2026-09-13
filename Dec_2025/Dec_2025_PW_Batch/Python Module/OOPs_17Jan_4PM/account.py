# Encapsulation
# class definition
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        # self.__balance = balance # private attribute
    
    # adding the money to the account
    def deposit(self, amount):
        self.balance += amount
    
    # withdraw the money from the account
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    # display the account details
    def display(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")



# Inheritance: SavingsAccount inherits from the Account
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    # display the savings account details
    # polymorphism
    def display(self):
        print(f"Saving Account Number: {self.account_number}, Balance: {self.balance}, Interest Rate: {self.interest_rate}")

    # add the interest in the savings account
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: {interest}. New Balance: {self.balance}")

# Inheritance: CurrentAccount inherits from Account
class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    # polymorphism: implementation of withdraw method
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdraw {amount}. New balance: {self.balance}")
        else:
            print("Overdraft limit exceeded")
    
    # polymorphism: implementation of display method
    def display(self):
        print(f"Current Account: {self.account_number}, Balance: {self.balance}, Overdraft Limit: {self.overdraft_limit}")


# create the object of the class
acc_priya = SavingsAccount(account_number=101, balance=10000, interest_rate=3)
acc_harsh = CurrentAccount(account_number=102, balance=30000, overdraft_limit=25000)

acc_harsh.deposit(50000)
acc_harsh.display()
acc_harsh.withdraw(85000)




        