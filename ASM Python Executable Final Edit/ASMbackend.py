import sys
import csv

class User:

    def __init__(self,admin,username,password,email,mobile,team,available):
        self.admin = admin
        self.username = username
        self.password = password
        self.email = email
        self.mobile = mobile
        self.team = team
        self.available = available
        
    
    def get_admin(self):
        return self.admin
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def get_email(self):
        return self.email
    
    def get_mobile(self):
        return self.mobile

    def get_team(self):
        return self.team
    
    def get_available(self):
        return self.available




class UserManager:

    def __init__(self):
        self.users = []




    def log_in(self,username,password):
        num_of_users = len(self.users)
        i = 0
        try:
            while (i<num_of_users):
                sort_username = str(self.users[i].get_username())
                sort_password = str(self.users[i].get_password())
                if (sort_username == username):
                                    if (sort_password == password):
                                        user_index_position = i
                                        return user_index_position
                                    else:
                                        sys.stdout.write("\nWrong username/password")
                                        i = num_of_users + 1
                                        
                                    
                else:
                    i += 1
        except:
            sys.stdout.write("No user found. Try restarting the program and adding a user.")

    #This function is for the admin to change their attributes, cannot use user_index_position
    #variable as the admin can change the entire list, so I'm searching for username and password
    #before changing anything. Not proud of this block, only one line different.
    def find_user_change_attribute(self,username,password,attribute,value):
        num_of_users = len(self.users)
        i = 0
        try:
            while (i<num_of_users):
                sort_username = str(self.users[i].get_username())
                sort_password = str(self.users[i].get_password())
                if (sort_username == username):
                                    if (sort_password == password):
                                        user_index_position = i
                                        self.users[i].available = value
                                        return user_index_position
                                    else:
                                        sys.stdout.write("\nWrong username/password.")
                                        i = num_of_users + 1
                                    
                else:
                    i += 1
        except:
            sys.stdout.write("Could not find matching user.")

    def log_in_admin(self,user_index_position):
        try:
            sort_admin = str(self.users[user_index_position].get_admin())
            user_is_admin = sort_admin
            return user_is_admin
        except:
            login_error = True
            return login_error





    def add_user(self,admin,username,password,email,mobile,team,available):
        self.users.append(User(admin,username,password,email,mobile,team,available))

    def del_user(self,list_index):
        try:
            del self.users[list_index]
        except:
            sys.stdout.write("\nError, user does not exist.")




    #could have one of these for each user attribute. leave_team, edit_team, edit_mobile etc.
    def leave_team(self,user_index_position):
        i = user_index_position
        self.users[i].team = "None"

    def edit_available(self,user_index_position,value):
        i = user_index_position
        self.users[i].available = value
        



    def get_all_users(self):
        all_users = ""
        num_of_users = len(self.users)
        i = 0
        while (i<num_of_users):
            a_user = ""
            a_user += str(i) + ": "
            a_user += self.users[i].get_admin() + ", "
            a_user += self.users[i].get_username() + ", "
            a_user += self.users[i].get_email() + ", "
            a_user += self.users[i].get_mobile() + ", "
            a_user += self.users[i].get_team() + ", "
            a_user += self.users[i].get_available()
            all_users += a_user + "\n"
            i += 1
        return all_users




    def get_user_attributes(self,user_index_position):
        i = user_index_position
        a_user = ""
        a_user += self.users[i].get_admin() + ", "
        a_user += self.users[i].get_username() + ", "
        a_user += self.users[i].get_password() + ", "
        a_user += self.users[i].get_email() + ", "
        a_user += self.users[i].get_mobile() + ", "
        a_user += self.users[i].get_team() + ", "
        a_user += self.users[i].get_available() + "\n"
        return a_user




    def get_team_users(self,value):
        sorted_users = ""
        num_of_users = len(self.users)
        i = 0
        while (i<num_of_users):
            sort_team = str(self.users[i].get_team())
            if (sort_team == value):
                a_user = ""  
                a_user += self.users[i].get_username() + ", "
                a_user += self.users[i].get_email() + ", "
                a_user += self.users[i].get_mobile() + ", "
                a_user += self.users[i].get_team() + ", "
                a_user += self.users[i].get_available()
                sorted_users += a_user + "\n"
                i += 1
            
            else:
                i += 1
        return sorted_users
            


        
    def save_file(self):
        save_csv = open("userdata.csv","w")
        num_of_users = len(self.users)
        i = 0
        while (i < num_of_users):
            save_csv.write(str(self.users[i].admin)+ "," +
                                str(self.users[i].username)+ "," +
                                str(self.users[i].password)+ "," +
                                str(self.users[i].email)+ "," +
                                str(self.users[i].mobile)+ "," +
                                str(self.users[i].team)+ "," +
                                str(self.users[i].available) + "\n")
            i += 1
        save_csv.close()




    def load_file(self):
        self.users = []
        try:
            with open("userdata.csv", "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    admin = str(line[0])
                    username = str(line[1])
                    password = str(line[2])
                    email = str(line[3])
                    mobile = str(line[4])
                    team = str(line[5])
                    available = str(line[6])
                    self.add_user(admin,username,password,email,mobile,team,available)
                    #unhash for troubleshooting
                    #print(self.users)
        except:
            sys.stdout.write("\n\nLoad Error, userdata.csv file not found, ignore if you're "
                             + "adding the first user. To add a new user, reload the program and "
                             + "enter \"n\"\n")
