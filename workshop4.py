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
    
    def transfer_money(self, amount, to_user, pin):
        print(f"\nYou are transferring ${amount} to {to_user.name}")
        print("Authentication required")
        entered_pin = input("Enter your PIN: ")
        
        if entered_pin != pin:
            print("Transfer failed: Incorrect PIN.")
            return False
        
        if amount <= self.balance:
            self.balance -= amount
            to_user.balance += amount
            print("Transfer authorized")
            print(f"Transferring ${amount} to {to_user.name}")
            return True
        else:
            print("Insufficient funds for this transfer.")
            return False

    def request_money(self, from_user, amount):
        print(f"\nYou are requesting ${amount} from {from_user.name}")
        print("User authentication is required...")
        entered_pin = input(f"Enter {from_user.name}'s PIN: ")
        entered_password = input("Enter your password: ")
        
        if entered_pin == from_user.pin and entered_password == self.password:
            if amount <= from_user.balance:
                from_user.balance -= amount
                self.balance += amount
                print("Request authorized")
                print(f"{from_user.name} sent ${amount}")
            else:
                print(f"{from_user.name} has insufficient funds to fulfill the request.")
        else:
            print("Request failed: Incorrect credentials.")

    def show_balance(self):
        print(f"{self.name} has an account balance of: {self.balance}")

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

# bank_user = BankUser("Bob", 1234, "password", 0)
# bank_user.show_balance()
# bank_user.deposit(1000)
# bank_user.show_balance()
# bank_user.withdraw(500)
# bank_user.show_balance()

# Driver Code for Task 5
user1 = BankUser("Alice", "1234", "alicepassword")

user2 = BankUser("Bob", "5678", "bobpassword")

user1.deposit(5000)

user2.deposit(900)

user1.show_balance()
user2.show_balance()

if user2.transfer_money(500, user1, "5678"):
    user1.show_balance()
    user2.show_balance()

user1.request_money(user2, 250)

user1.show_balance()
user2.show_balance()
