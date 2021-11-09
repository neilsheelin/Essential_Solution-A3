import sys

#This is still heavily WIP, at the moment I've gone with no frontend/backend as
#I wish to keep it to one simple file to submit. This may change if it becomes
#too complicated.

class UI:

    def __init__(self):

        #menu decor
        bars = "\n================================================================"

        #initial login menu assets
        login_menu = bars
        login_menu += "\n\nWelcome to the Australian Sports Manager (ASM)"
        login_menu += "\n" + bars
        login_menu += "\n\nExisting user? (Y/N): "

        #create user menu assets
        create_um = bars
        create_um += "\n\nCreate a New ASM User"
        create_um += bars
    
        #standard menu assets
        std_menu = ""

        #admin menu assets
        adm_menu = ""

        option = UI.get_yn(login_menu)

        if (option == "y"):
            user_name = UI.get_string("\nPlease enter username: ")
            password = UI.get_string("Please enter password: ")

        elif (option == "n"):
            pass

        else:
            pass

    #returns an integer from the user
    def get_integer(prompt):
        pass

    #returns a string from the user
    def get_string(prompt):
        sys.stdout.write(prompt)
        user_input = sys.stdin.readline().strip()
        while (user_input == ""):
            sys.stdout.write("Please try again: ")
            user_input = sys.stdin.readline().strip()
        return user_input

    #returns a yes or no from the user
    def get_yn(prompt):
        sys.stdout.write(prompt)
        user_input = sys.stdin.readline().lower().strip()
        while (user_input != "y" and user_input != "n"):
            sys.stdout.write("Please enter Y or N: ")
            user_input = sys.stdin.readline().lower().strip()
        return user_input
            


class User:

    def __init__(self,admin,username,email,mobile,available):
        self.admin = False
        self.username = username
        self.email = email
        self.mobile = mobile
        self.available = ""

class UserManager:

    def __init__(self)

initialise = UI()
        
        
