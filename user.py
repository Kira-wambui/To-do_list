class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_id(self):
        return self.username

    @staticmethod
    def get(username):
        # Retrieve user from database or data store
        # Replace this with your actual database query or ORM call
        users = {'user': User('user', 'password')}  # Example user data
        return users.get(username)
