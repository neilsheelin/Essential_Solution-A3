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
        UM = UserManager()
        

        if (option == "n"):
            pass

        elif (option == "y"):
            username = UI.get_string("\nPlease enter username: ")
            password = UI.get_string("Please enter password: ")
            UM.log_in(username, password)
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

    def clear_console():
        os.system("cls" if os.name == "nt" else "clear")
            


class User:

    def __init__(self,admin,username,password,email,mobile,available):
        self.admin = False
        self.username = username
        self.password = password
        self.email = email
        self.mobile = mobile
        self.available = ""

class UserManager:

    def __init__(self):
        self.users = []

    def log_in(self, username, password):
        print(username + " " + password)

    def add_user(self,admin,username,password,email,mobile,available):
        self.users.append(User(admin,username,password,email,mobile,available))

    def save_file(self):
        pass

    def load_file(self):
        try:
            with open("userdata.csv", r) as load_csv:
                self.users = []
                i = 0
                while (i == 0):
                    try:
                        load_contents = load_csv.readline()
                        attributes = load_csv.split(",")
                        admin = attributes[0]
                        username = attributes[1]
                        password = attributes[2]
                        email = attributes[3]
                        mobile = attributes[4]
                        available = attributes[5]
                        self.add_user(admin,username,password,email,mobile,available)
                    except:
                        i = 1
        except:
            sys.stdout.write("userdata.csv could not be found.")
                    
                

initialise = UI()
        
        
