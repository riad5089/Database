import sys
from database import Dbhelper
class FLipkart:
    def __init__(self):
        #to connnct to the database
        self.db=Dbhelper()
        self.menu()
    def menu(self):
        user_input=input("""
        1.Enter 1 to register
        2.Enter 2 to login
        3.Anything else to leave
        """)
        if user_input=="1":
            self.register()
        elif user_input=="2":
            self.login()
        else:
            sys.exit(110)

    def login_menu(self):
        input("""
        1.Enter 1 to see profile
        2.Enter 2 to edit profit
        3.Enter 3 to delete profit
        4.Enter 4 to logout
        """)

    def  register(self):
        name=input("Enter the name")
        email=input("enter the email")
        password=input("Enter the password")
        response=self.db.register(name,email,password)
        if response:
            print("Registration successful")

        else:
            print("Registration failed")
        self.menu()
    def login(self):
        email=input("Enter a email")
        password=input("Enter a password")
        data=self.db.search(email,password)
        # if len(data)==0:
        if len(data)==0:
            print("Incorrenct email/password")
            self.login()
        else:
            print("hello",data[0][1])
            self.login_menu()
obj=FLipkart()
