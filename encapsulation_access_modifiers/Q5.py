"""Create a class User with:
username (public)
__password (private)
Write a method check_login() to validate the password."""

class User:
    def __init__(self, userName, password):
        self.userName = userName
        self.__password = password

    def check_login(self, enterPass):
        if enterPass == self.__password:
          return  "login successfull"
        else:
            return "login failed"


user1 = User("maryam" , "alina123")
print(user1.check_login("alina123"))



       
