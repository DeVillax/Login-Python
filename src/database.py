import sqlite3      # Import sqlite3 module to work with databases.

class Database():
    #Define Database class, this class contains methods used to create a database to store users login data.

    def __init__(self,database_name):
        # This method will inizialise the Database class. An argument containing the database name is passed to the class.
        
        self.database = sqlite3.connect(database_name) #create/connect the database
        self.cursor = self.database.cursor()

    def create_table(self):
        # Creates the table 'usernames'
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usernames (Name text, Surname text, Email text, Username text, Password text)''') 
        self.database.commit()

    def insert_row(self,name,surname,username,password):
        # Insert a row into the usernames database. It does not check whether the arguments are valid.

        self.cursor.execute('''INSERT INTO usernames (Name,Surname,Username,Password) values (?,?,?,?)''',(name,surname,username,password))
        self.database.commit()
        
    def retrieve_user(self,username):
        # Retrieves a user from the database. The method receives an username as an argument.

        self.data = self.cursor.execute('''SELECT * FROM usernames WHERE username = ?''', (username,))
        for row in self.data:
            return row

