# Login-Python
Simple login application on Tkinter. It uses a database (sqlite3) to store usernames and passwords, which are checked once the user enter 
its credentials.

## 1) Project Overview

Users will be prompted with a login screen with two buttons, a log in one and a sign up one. If an user does not have an account created
in the system, it will not be able to log into the system. Therefore, users can create an account by providing its first name, surname, email,username and a password. Once the account is created, users will be able to log in succesfully.

User will be able to log in using its username or email address.

## 2) Input Considerations

There are five inputs in this application.

* **First name** 
Field to enter information related to user´s first name. Numbers are allowed.
* **Surname**
Information related to user's surname. Numbers are also allowed in this field. 
* **Email Address**
Users will need to enter a valid email address that must exists (e.g. yourvalidemail@validDomain.com). If users don't enter a valid email address, they will be prompted with an error message asking them to enter a valid one.
* **Username**
This need to be a non-existing one as the application does not accept duplicates. Therefore, if user enters a username which is already taken, an error message will be displayed.
* **Password**
This will be the key to access the application. Password must be 8 character or longer, it must have at least an uppercase letter, a number and one special character"

## 3) Output Considerations

Once the user signs up in the application sucessfully, a message will be displayed to inform them the an account has been sucessfully created. If user logs in successfully, they will be prompted with a message that they have sucessfully logged into the application.

## 4) Testing environment

Python 3.7

## 5) How to run the code 
 
 ### 5.1) Running the code
  This program can be launched through the system console by accessing the directory where files are and executing the following 
  command line.
   
  python app.py
  
  The program will display the Log In Frame.
   
## 6) General Information
  
  The code contains comments to easily understand what each method is in charge of.
  

 
    


    
