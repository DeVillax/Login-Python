import tkinter as tk                # import tkinter module
import re                           # import regex module to use regular expresions
from Database import Database       # import Database class
from tkinter import messagebox      # import messagbox from tkinter module

class App(tk.Tk):
    # Base class in Tkinter
    
    def __init__(self):
        # Initialises the app and display the LoginFrame.
        
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(LoginFrame)

    def switch_frame(self, frame_class):
        # Destroys current frame and replaces it with a new one.
        
        self.new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = self.new_frame
        self._frame.pack()


class LoginFrame(tk.Frame):
    # Login Frame to access the app.

    def __init__(self, master):
        # Initialises the Login Frame.
        
        super().__init__(master)

        master.title("Log in")

        # Declaring Labels
        
        self.label_username = tk.Label(self,text = "Username")
        self.label_password = tk.Label(self,text = "Password")

        # Declaring Entries
        self.entry_username = tk.Entry(self)
        self.entry_password = tk.Entry(self,show = "*")
        
        # Placing Labels and Entries in a Grid
        
        self.label_username.grid(row=0)
        self.label_password.grid(row=1)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        # Seting up a Log In Button

        self.logbtn = tk.Button(self,text = "Log in",command=self.login_btn_clicked)
        self.logbtn.grid(row=3, column = 0, sticky = "ew")

        # Seting up a Sign Up Button

        self.create_new_user_button = tk.Button(self,text = "Sign up",command=lambda: master.switch_frame(SignUpFrame))
        self.create_new_user_button.grid(row = 3, column = 1, sticky = "e")

        self.pack()

    def login_btn_clicked(self):
        # Defines the behaviour of the app when the users click on the Log in button

        # Retrieving the data from the entries.
        
        self.username = self.entry_username.get()
        self.password = self.entry_password.get()

        if len(self.username) == 0 and len(self.password) == 0:
            # Displays an error message if both username and password entries are empty

            messagebox.showerror("Login Info", "Please enter username and password")
        elif len(self.username) == 0:
            # Display an error message if the username entry if empty
            
            messagebox.showerror("Login Info", "Please enter your username")
        elif len(self.password) == 0:
            # Display an error message if the password entry is empty

            messagebox.showerror("Login Info", "Please enter your password")
        else:
            self.database = Database("usernames.db")                # Connect to the Usernames database
            self.database.create_table()                            # Create an usernames table if does not exists
            self.check = self.database.retrieve_user(self.username) # Retrieve an unsername from the Usernames database
            
            if self.check is None:
                # An error message will be displayed if the username does not exist
                
                messagebox.showerror("Login Info", "This username does not exists")
            else:
                if self.username == self.check[3] and self.password == self.check[4]:
                    # If username is correct and the password entered is correct, a gretting message will be displayed

                    messagebox.showinfo("Login info", "Welcome " + self.check[0])            
                else:
                    # If either username or password are not correct, users will be prompted with an error message.
                    
                    messagebox.showerror("Login error", "Incorrect username or password.")


class SignUpFrame(tk.Frame):
    # Sign Up Frame to create a new user.

    def __init__(self,master):
        # Initialises the Sign Up Frame.
        super().__init__(master)

        master.title("Sign Up")

        # Declaring Labels
        
        self.information_label = tk.Label(self,text = "All fields are mandatory")
        self.name_label = tk.Label(self,text = "Name")
        self.surname_label = tk.Label(self,text = "Surname")
        self.email_label = tk.Label(self,text = "Email")
        self.username_label = tk.Label(self,text = "Username")
        self.password_label = tk.Label(self,text = "Password")
        
        # Declaring Entries
        
        self.name_entry = tk.Entry(self)
        self.surname_entry = tk.Entry(self)
        self.email_entry = tk.Entry(self)
        self.username_entry = tk.Entry(self)
        self.password_entry = tk.Entry(self,show = "*")

        # Placing Labels and Entries in the grid
        
        self.information_label.grid(row = 0, column = 1, sticky = "w")

        self.name_label.grid(row = 1, column = 0, sticky = "w")
        self.name_entry.grid(row = 1, column = 1)

        self.surname_label.grid(row = 2, column = 0, sticky = "w")
        self.surname_entry.grid(row = 2, column = 1)

        self.email_label.grid(row = 3, column = 0, sticky = "w")
        self.email_entry.grid(row = 3, column = 1, sticky = "w")

        self.username_label.grid(row = 4, column = 0, sticky = "w")
        self.username_entry.grid(row = 4, column = 1)

        self.password_label.grid(row = 5, column = 0, sticky = "w")
        self.password_entry.grid(row = 5, column = 1)

        # Declaring and placing buttons
        
        self.return_button = tk.Button(self, text = "Return", command = lambda: master.switch_frame(LoginFrame))
        self.return_button.grid(row = 6, column = 0, sticky = "w")
        
        self.submit_button = tk.Button(self, text = "Submit", command = self.createUser)
        self.submit_button.grid(row = 6, column = 1, sticky = "e")
                
    def createUser(self):
        # Insert an user in the database

        # Retrieve the content entered in the Entries
        
        self.name_entry_content = self.name_entry.get()
        self.surname_entry_content = self.surname_entry.get()
        self.username_entry_content = self.username_entry.get()
        self.password_entry_content = self.password_entry.get()
        self.email_entry_content = self.email_entry.get()

        if self.validate_data(self.name_entry_content,self.surname_entry_content,
                             self.username_entry_content,self.password_entry_content,
                             self.email_entry_content):
            
            # Call methods to validate if entered data is correct.Then, it will create the table if doesnt exists
            # and insert the user information in the database. Once an user has been inserted, the app will switch
            # the Sign Up Frame for the Log In Frame.
            
            self.database.create_table()

            self.database.insert_row(self.name_entry_content,self.surname_entry_content,
                                     self.username_entry_content,self.password_entry_content)

            self.master.switch_frame(LoginFrame)
            

    def validate_data(self,
                     name,surname,
                     username,password,
                     email):
        # Checks whether the data entered is valid by calling its respective methods.
        
        if self.validate_name(name) and self.validate_surname(surname) and self.validate_email(email) and self.validate_username(username) and self.validate_password(password):
            return True

    def validate_name(self,name):
        # Checks whether the surname field is empty
        
        if len(name) == 0:
            messagebox.showerror("Sign Up Info", "Please input a Name")
        else:
            return True

    def validate_surname(self,surname):
        # Checks whether the surname field is empty
        
        if len(surname) == 0:
            messagebox.showerror("Sign Up Info", "Please input a Surname")
        else:
            return True

    def validate_password(self, password):
        # Checks whether the password entered is at least 8 characters long, contains an uppercase, a number and a special character
        if len(password) == 0:
            messagebox.showerror("Sign Up Info", "Please enter a password")
        else:
            if len(password) < 8:
                messagebox.showerror("Sign Up Info","The password cannot be less than 8 characters")
            elif not re.search(r"[A-Z]", password):
                messagebox.showerror("Sign Up Info","The password must contain an uppercase letter")
            elif not re.search(r"[!@#]", password):
                messagebox.showerror("Sign Up Info","The password must contain one special character")
            else:
                return True
        
    def validate_username(self, username):
        # Checks whether the username entered does not already exits in the database

        if len(username) == 0:
            messagebox.showerror("Sign Up Info", "Please enter an username")
        else:
            self.database = Database("usernames.db")
            if self.database.retrieve_user(username) == None:
                return True
            else:
                messagebox.showerror("Sign Up Info", "The username already exists. Please select other one")
                return False
        
    def validate_email(self,email):
        # Checks whether the email entered is valid.

        if len(email) == 0:
            # Checks whether user have entered data in the email entry.
            
            messagebox.showerror("Sign Up Info", "Please enter an email address")
        else:
            if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",email):
                # There must be a @ and a . to be valid
                
                return True
            else:
                messagebox.showerror("Sign Up Info", "The email entered is not valid")
                return False
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
