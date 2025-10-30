import os

class LoginSystem:

    def __init__(self, my_users_data="users.txt"):
        self.my_users_data = my_users_data
        open(self.my_users_data, "a").close()


    def signup(self):
        username = input("username :")
        password = input("password :")

        with open(self.my_users_data, "a") as file:
            file.write(f"{username}:{password}\n")
            print("Registration was successful.")
            

        with open(self.my_users_data, "r") as file:
            for line in file:
                user = line.strip().split(":")
                if user == username:
                    print("This username already exists.")
                    return

    def login(self):
        username = input("username :")
        password = input("password :")

        with open(self.my_users_data, "r") as file:
            for line in file:
                username , password == line.strip().split(":")
                if username == username and password == password:
                    print("Wellcome!")
                else:
                    print("The username or password is incorrect.")

    def menu(self):
        while True:
            print("*** LoginSystem ***")
            print("1. signup")
            print("2. login")
            print("3. exit")
            
            choice = input("Enter your choice :")

            if choice == "1":
                self.signup()
            elif choice == "2":
                self.login()
            elif choice == "3":
                print("Goodby")
            else:
                print("Invalid option")

system = LoginSystem()
system.menu()


# __name__ == "__main__"


