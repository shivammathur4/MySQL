'''
@Author: Shivam Mathur
@Date: 19-07-2021
@Last Modified time: 19-07-2021
@Title : This script provides function for performing create,show,drop
         and establish connection with MySQL.
'''
import os
import mysql.connector
from dotenv import load_dotenv
from loggers import logger

load_dotenv()

class ViewFunction:

    def __init__(self):
        '''
        Description:
            created constructor and test mysql database connection.
        Parametter:
            it takes self as parameter.
        '''
        self.db_connection = mysql.connector.connect(
            host=os.getenv('host'),
            user=os.getenv('user'),
            passwd=os.getenv('passwd'),
            auth_plugin=os.getenv('auth_plugin')
        )
        self.db_cursor = self.db_connection.cursor()

    
    def print_connection(self):
        '''
        Description:
            this function prints the connection object.
        '''
        
        try:
            print(self.db_connection)
        
        except Exception as e:
            logger.error(e)
    
    
    def create_views(self):
        '''
        Description:
            Methods create views from existing tables.
        '''
        try:
            self.db_cursor.execute("USE DB1")
            self.db_cursor.execute('''CREATE VIEW customer1 AS SELECT name, age FROM customers''')
            print("View created")
        except Exception as ex:
            logger.error(ex)
    
    def display_views(self):
        '''
        Description:
            This function displays the view.
        
        '''

        try:
            self.db_cursor.execute("SELECT * FROM customer1")
            result = self.db_cursor.fetchall()

            for x in result:
                print(x)
        
        except Exception as e:
            logger.error(e)


    def update_view(self):
        '''
        Description:
            This function updates the view.
      
        '''

        try:
            self.db_cursor.execute('''ALTER VIEW customer1 AS SELECT 
                    name, age FROM customers''')
            logger.info("View Updated")
        
        except Exception as e:
            logger.error(e)        

    
    def drop_views(self):
        '''
        Description:
            Drop view which are existing in the database.    
        '''
        try:
            self.db_cursor.execute("DROP VIEW customers1")
            print("View Dropped")
        except Exception as ex:
            logger.error(ex)

    

if __name__ == "__main__":
    view = ViewFunction()
    view.print_connection()
    view.create_views()
    view.display_views()
    view.drop_views()
   