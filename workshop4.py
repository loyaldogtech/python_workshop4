class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password

class BankUser(User):
    def __init__(self, name, pin, password, balance=0):
        super().__init__(name, pin, password)
        self.balance = float(balance)

    def show_balance(self):
        print(f"{self.name} has and account balance of: ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


# Driver Code for Task 1 
# user = User("Bob", 1234, "password")
# print(user.name, user.pin, user.password)

# # Driver Code for Task 2
# user.change_name("Rob")
# user.change_pin(4321)
# user.change_password("rob1234")
# print(user.name, user.pin, user.password)

# Driver Code for Task 3
# bank_user = BankUser("Bob", 1234, "password", 0)
# print(bank_user.name, bank_user.pin, bank_user.password, bank_user.balance)

# Driver Code for Task 4

bank_user = BankUser("Bob", 1234, "password", 0)
bank_user.show_balance()
bank_user.deposit(1000)
bank_user.show_balance()
bank_user.withdraw(500)
bank_user.show_balance()
