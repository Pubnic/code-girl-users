from uuid import uuid4

class UserDatabase:
    users = []
    
    def __init__(self):
        pass  # Iniciar a conexão com o banco na tabela User

    def add_user(self, user: dict):
        user['id'] = str(uuid4())
        self.users.append(user)
        return user

    def get_user(self, user_id: str):
        for user in self.users:
            if user['id'] == user_id:
                return user
        return None

    def get_users(self):
        return self.users
    
    def update_user(self, new_user: dict):
        for index, user in enumerate(self.users):
            if user['id'] == new_user['id']:
                self.users[index] = new_user
                return new_user
        return None

    def delete_user(self, user_id: str):
        for index, user in enumerate(self.users):
            if user['id'] == user_id:
                self.users.pop(index)
                return True
        return False
