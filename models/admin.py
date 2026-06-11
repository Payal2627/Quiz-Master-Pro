class Admin:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display_admin(self):
        print("\nAdmin Details")
        print("Username:", self.username)