class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, new_password):
        if (len(new_password) == 0):
            print("Пароль не должен быть пустым")
        else:
            self.password = new_password
            print("Пароль успешно изменен")

    def check_password(self, password):
        return self.password == password


user = UserAccount("john", "john@example.com", "qwerty1234")

user.set_password("")
user.set_password("12345678")
print(user.check_password("12345678"))
