'''
@Author: Shivam Mathur
@Date: 23-07-2021
@Last Modified time: 23-07-2021
@Title : This script provides function for performing create,show,drop
         and establish connection with MySQL.
'''
import os
import mysql.connector
from dotenv import load_dotenv
from loggers import logger

load_dotenv()

class WindowFunctions:

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
    
    
    def ranking_function(self):
        '''
        Description:
            This function implemented group by for ranking functions.
        
        '''

        try:
            self.db_cursor.execute('''SELECT ROW_NUMBER() OVER (PARTITION BY Department ORDER BY Salary DESC) AS emp_row_no, Name,  Department, Salary, RANK() OVER(PARTITION BY Department 
                                   ORDER BY Salary DESC) AS emp_rank, DENSE_RANK() OVER(PARTITION BY Department ORDER BY Salary DESC) AS emp_dense_rank, FROM employee ;''')
            result = self.db_cursor.fetchall()
            for x in result:
                print(x)
        

        except Exception as e:
            logger.error(e)


    def analytical_function(self):
        '''
        Description:
            This function implemented group by for analytical functions.
        Parameter:
            it takes self as parametr.
        '''

        try:
            self.db_cursor.execute('''SELECT Name, Age, Department, Salary, AVERAGE(Salary) OVER( PARTITION BY Department ORDER BY Age) AS Avg_Salary FROM employee;''')
            result = self.db_cursor.fetchall()
            for x in result:
                print(x)
        

        except Exception as e:
            logger.error(e)        

if __name__ == "__main__":
    window = WindowFunctions()
    window.print_connection()
    window.ranking_function()
    window.analytical_function()