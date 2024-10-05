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









# Driver Code for Task 1 
user = User("Bob", 1234, "password")
print(user.name, user.pin, user.password)

# Driver Code for Task 2
user.change_name("Rob")
user.change_pin(4321)
user.change_password("rob1234")
print(user.name, user.pin, user.password)

