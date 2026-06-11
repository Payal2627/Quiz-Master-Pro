class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display_user(self):
        print("\nUser Details")
        print("Username:", self.username)