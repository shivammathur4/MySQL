'''
@Author: Shivam mathur
@Date: 20-07-2021
@Last Modified time: 20-07-2021
@Title : This Script have methods to implement inner join,left join
         right join in MySQL Database.
'''

import sys
sys.path.insert(0, '/home/shivammathur/MySQL')
from log import logger

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mydb=mysql.connector.connect(
     host = os.environ.get("DB_HOST"),
     user = os.environ.get("DB_USER"),
     passwd= os.environ.get("DB_PASSWORD"),
     database = os.environ.get("DATABASE"))


class Joins_Methods():

    
    def inner_join(self):
        '''
        Description:
            Method implement inner join between two tables on id column.
        Parameters:
            Object of this(Joins_Methods) class.
        Return:
            None.
        '''
        try:
            mycursor = mydb.cursor()
            query="SELECT STUDENT.NAME from STUDENT from INNER JOIN Student on Student.Roll_no = STUDENT.Roll_no"
            mycursor.execute(query)
            result_set = mycursor.fetchall()
            print(result_set)
        except Exception as ex:
            logger.error(ex)
    
    def left_join(self):
        '''
        Description:
            Method implement left join between two tables on column id.
        Parameters:
            Object of this(Joins_Methods) class.
        Return:
            None.
        '''
        try:
            mycursor = mydb.cursor()
            query ="SELECT STUDENT.NAME from STUDENT from LEFT JOIN Student on Student.Roll_no = STUDENT.Roll_no"
            mycursor.execute(query)
            result_set = mycursor.fetchall()
            print(result_set)
        except Exception as ex:
            logger.error(ex) 
    
    def right_join(self):
        '''
        Description:
            Method implement right join between two tables on column id.
        Parameters:
            Object of this(Joins_Methods) class.
        Return:
            None.
        '''
        try:
            mycursor = mydb.cursor()
            query="SELECT STUDENT.Name from STUDENT from RIGHT JOIN Student on Student.Roll_no = STUDENT.Roll_no"
            mycursor.execute(query)
            result_set = mycursor.fetchall()
            print(result_set)
        except Exception as ex:
            logger.error(ex)

    

op = Joins_Methods()
op.inner_join()
op.right_join()
op.left_join()
