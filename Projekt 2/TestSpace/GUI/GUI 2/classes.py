class Credentials:
    def __init__(self, username, password, admin=False):
        self.username = username
        self.password = password
        self.admin = admin

    def __str__(self):
        return f"Username: {self.username}, Password: {self.password}"