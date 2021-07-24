'''
@Author: Shivam Mathur
@Date: 22-07-2021
@Last Modified time: 22-07-2021
@Title : This script provides function for performing create,show,drop
         and establish connection with MySQL.
'''
import os
import mysql.connector
from dotenv import load_dotenv
from loggers import logger

load_dotenv()

class INDEXES:

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
    
    
    

    def create_index(self):
        '''
        Description:
            This function creates a index.
        '''

        try:
            self.db_cursor.execute("DB1")
            self.db_cursor.execute("CREATE INDEX idx_name ON customers (name)")
            print("Index created")

        except Exception as e:
            logger.error(e)


    def display_index(self):
        '''
        Description:
            This function shows the index on table.
        
        '''

        try:
            self.db_cursor.execute("SHOW INDEX FROM customers")
            result = self.db_cursor.fetchall()
            for x in result:
                print(x)

        except Exception as e:
            logger.error(e)

    
    def select(self):
        '''
        Description:
            This function select and dispalys name string 
        
        '''

        try:
            self.db_cursor.execute("EXPLAIN SELECT * FROM customers WHERE name LIKE 'A%")
            result = self.db_cursor.fetchall()
            for x in result:
                print(x)
        
        except Exception as e:
            logger.error(e)

    def drop_index(self):
        '''
        Description:
            This function drops the index from table.
       
        '''

        try:
            self.db_cursor.execute("DROP INDEX customers.idx_name")
            print("Index Dropped")

        except Exception as e:
            logger.error(e)        

if __name__ == "__main__":
    index = INDEXES()
    index.print_connection()
    index.create_index()
    index.display_index()
    index.select()
    index.drop_index()