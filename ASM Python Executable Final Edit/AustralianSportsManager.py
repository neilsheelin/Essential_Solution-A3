import sys
import ASMbackend

class UI:

    def __init__(self):

        #menu decor assets
        bars = "\n============================================================================="
        title_s = "\n Username | Email | Mobile | Team | Availability"
        title_l = "\n List Position | Admin | Username | Email | Mobile | Team | Availability"
        title_xl = "\n Admin | Username | Password | Email | Mobile | Team | Availability"
        #initial start menu
        start_menu = bars
        start_menu += "\n> Welcome to the Australian Sports Manager (ASM) "
        start_menu += bars
        start_menu += "\n\nAre you an existing user? (Y/N): "
        #create user menu 
        create_um = bars
        create_um += "\n> Creating a New ASM User "
        create_um += bars
        #login menu
        login_menu = bars
        login_menu += "\n> Logging Into Your ASM User Account "
        login_menu += bars
        #admin menu
        admin_menu = bars
        admin_menu += "\n> ASM Admin User Menu "
        admin_menu += bars
        admin_menu += "\n\n1. View all user data."
        admin_menu += "\n2. Remove a user."
        admin_menu += "\n3. Add an example user."
        admin_menu += "\n4. Change your availability."
        admin_menu += "\n5. List members in a team."
        admin_menu += "\n6. Save all changes." 
        admin_menu += "\n7. Log out."
        admin_menu += "\n\nSelect an option (1-7): "
        #standard user menu
        user_menu = bars
        user_menu += "\n> ASM Standard User Menu "
        user_menu += bars
        user_menu += "\n\n1. View your details."
        user_menu += "\n2. Change your availability."
        user_menu += "\n3. Leave your team."
        user_menu += "\n4. Save all changes."
        user_menu += "\n5. Log out."
        user_menu += "\n\nSelect an option (1-5): "






        #existing user and create new user block
        self.UM = ASMbackend.UserManager()
        existing_user = UI.get_yn(start_menu)
        
        while (existing_user == "n"):
            sys.stdout.write(create_um)
            user_input = UI.get_yn("\n\nAre you an Admin/Official? (Y/N): ")
            
            if (user_input == "y"):
                admin = "True"
            else:
                admin = "False"
                
            username = UI.get_str("Please enter your username: ")
            password = UI.get_str("Please enter your password: ")
            email = UI.get_str("Please enter your email: ")
            mobile = UI.get_str("Please enter your mobile number (in the"
                                   + " format 0000-000-000): ")
            team = UI.get_str("Please enter your team name: ")
            available = UI.get_str("Please enter days available (in the"
                                      + " format DAY(7am-10pm) - DAY(...): ")
            self.UM.load_file()
            self.UM.add_user(admin,username,password,email,mobile,team,available)
            self.UM.save_file()
            sys.stdout.write("\nNew user record created...\n")
            existing_user = "y"







        #log into user block
        user_index_position = None
        sort_admin = None
        login_error = None
        user_is_admin = "False"
        
        while (user_index_position == None):
            self.UM.load_file()
            sys.stdout.write(login_menu)
            username = UI.get_str("\n\nPlease enter your username: ")
            password = UI.get_str("\nPlease enter your password: ")
            user_index_position = self.UM.log_in(username,password)
            login_error = self.UM.log_in_admin(user_index_position)
            user_is_admin = self.UM.log_in_admin(user_index_position)
            if (login_error == True):
                sys.stdout.write("\n\nNo matching user, try adding a new user...\n")
                initialise = UI()
            else:
                sys.stdout.write("\n\nLogged in successfully...\n")





                
            
        #menu options for admin users
        if (user_is_admin == "True"):

            menu_option = UI.get_str(admin_menu)

            while (menu_option != None):

                if (menu_option == "1"):
                    all_users = self.UM.get_all_users()
                    ud = bars
                    ud += "\n> Table of all user data: "
                    ud += bars
                    ud += title_l
                    ud += bars
                    ud += "\n" + all_users
                    sys.stdout.write(ud)
                    

                elif(menu_option == "2"):
                    all_users = self.UM.get_all_users()
                    ud = bars
                    ud += "\n> Select a user to remove, enter number >last list position to exit: "
                    ud += bars
                    ud += title_l
                    ud += bars
                    ud += "\n" + all_users
                    sys.stdout.write(ud)
                    list_index = UI.get_int("\nPlease enter list position: ")
                    self.UM.del_user(list_index)
                    sys.stdout.write("\nRemoved user at index position: " +str(list_index))

                elif(menu_option == "3"):
                    admin = "False"
                    username = "Example"
                    password = "User"
                    email = "example@user.com.au"
                    mobile = "112-358-1321"
                    team = "WSW"
                    available = "FRI(10am-7pm)"
                    self.UM.add_user(admin,username,password,email,mobile,team,available)
                    sys.stdout.write("\nExample user added...")

                elif(menu_option == "4"):
                    #originally intended for use to select attribute that they wish to edit
                    #but the admin shouldn't have such powers.
                    attribute = "available"
                    value = UI.get_str("Enter your availability (in the"
                                      + " format DAY(7am-10pm) - DAY(...): ")
                    self.UM.find_user_change_attribute(username,password,attribute,value)
                    sys.stdout.write("\nYour availability has been updated...")

                elif(menu_option == "5"):
                    value = UI.get_str("Enter team name: ")
                    sorted_users = self.UM.get_team_users(value)
                    ud = bars
                    ud += "\n> Displaying all users in team: "
                    ud += bars
                    ud += title_s
                    ud += bars
                    ud += "\n" + sorted_users
                    sys.stdout.write(ud)

                elif(menu_option == "6"):
                    self.UM.save_file()
                    sys.stdout.write("\n\nSaved to userdata.csv...")

                elif(menu_option == "7"):
                    initialise = UI()

                else:
                    sys.stdout.write("\nSorry, that's not an option.\n")

                menu_option = UI.get_str("\n" + admin_menu)







        #menu options for standard users    
        elif (user_is_admin == "False"):

            menu_option = UI.get_str(user_menu)

            while (menu_option != None):

                if (menu_option == "1"):
                    a_user = self.UM.get_user_attributes(user_index_position)
                    ud = bars
                    ud += "\n> Table of your user data: "
                    ud += bars
                    ud += title_xl
                    ud += bars
                    ud += "\n" + a_user
                    sys.stdout.write(ud)
                    
                elif(menu_option == "2"):
                    value = UI.get_str("Enter your availability (in the"
                                      + " format DAY(7am-10pm) - DAY(...): ")
                    self.UM.edit_available(user_index_position,value)
                    sys.stdout.write("\n\nYour availability has been updated...")

                elif(menu_option == "3"):
                    self.UM.leave_team(user_index_position)
                    sys.stdout.write("\nYou have left your team..")

                elif(menu_option == "4"):
                    self.UM.save_file()
                    sys.stdout.write("\n\nSaved to userdata.csv...")

                elif(menu_option == "5"):
                    initialise = UI()

                else:
                    sys.stdout.write("\nSorry, that's not an option.\n")

                menu_option = UI.get_str("\n" + user_menu)
        
        else:
            sys.stdout.write("User does not exist, please try again.")
            initialise = UI()








            
    #returns an integer from the user
    def get_int(prompt):
        sys.stdout.write(prompt)
        while True:
            try:
                user_input = int(sys.stdin.readline().strip())
                return user_input
            except:
                sys.stdout.write("Please enter a whole number: ")

    #returns a string from the user
    def get_str(prompt):
        sys.stdout.write(prompt)
        user_input = sys.stdin.readline().strip("\n")
        while (user_input == ""):
            sys.stdout.write("Please try again: ")
            user_input == sys.stdin.readline().strip()
        return user_input

    #returns a yes or no from the user
    def get_yn(prompt):
        sys.stdout.write(prompt)
        user_input = sys.stdin.readline().lower().strip()
        while (user_input != "y" and user_input != "n"):
            sys.stdout.write("Please enter Y or N: ")
            user_input = sys.stdin.readline().lower().strip()
        return user_input         

initialise = UI()
