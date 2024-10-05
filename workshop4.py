class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password











""" Driver Code for Task 1 """
user = User("Bob", 1234, "password")
print(user.name, user.pin, user.password)

