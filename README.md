# Login-Python
Simple login application on Tkinter. It uses a database (sqlite3) to store usernames and passwords, which are checked once the user enter 
its credentials.

1) Project Overview

Users will be prompted with a login screen with two buttons, a log in one and a sign up one. If an user does not have an account created
in the system, it will not be able to log into the system. Therefore, users can create an account by providing its first name, surname, email,username and a password. Once the account is created, users will be able to log in succesfully.

User will be able to log in using its username or email address.

2) Input Considerations

There are five inputs in this application.

1) First name, users will introduce a string containing information related to its first name, numbers are allowed in this field.
2) Surname, users will enter a string with information related to its surname name, numbers are also allowed in this field. 
3) Email Address, users will need to enter a valid email address that must exists as well (e.g. yourvalidemail@validDomain.com). If users do not enter a valid email address, they will be prompted with an error message asking them to enter a valid one.
4) Username, this need to be a valid one as the application does not accept duplicates. Therefore, if user enter a username which is already taken, an error message will be displayed.
5) Password, this will be the key to access the application. Password must to be 8 character or longer, it must have at least an uppercase letter, it must have at least a number and it needs to have at least one special character"

3) Output Considerations

Once the users sign up sucessfully in the application, a message will be displayed to inform them an user have been sucessfully created. If users log in successfully, they will be prompted with a message that they have sucessfully logged into the application.

4) Testing environment

Python 3.7

5) How to run the code and tests
 
 5.1) Running the code
  This program can be executed through the system console by accessing the directory where files are and executing the following 
  command line.
   
   python app.py
  
  The program will display the Log In Frame.
  
  5.2) Running tests
   Tests can be found in the test folder. They can be executed through the system console. Once the user is in the right folder where 
   modules are stored, the following commands will execute the tests.
   
   python test_app.py
   python test_database.py
   
 6) General Information
  
  The code contains comments to make it easier to understand what each method is in charge of.
  

 
    


    
