class Credentials:
    def __init__(self, username, password, admin=False):
        self.username = username
        self.password = self.set_admin(password)
        self.admin = admin
    
    def set_admin(self, admin):
        if admin == 1:
            return True
        else:
            return False

    def __str__(self):
        return f"Username: {self.username}, Password: {self.password}"