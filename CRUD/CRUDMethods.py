'''
@Author: Shivam Mathur
@Date: 19-07-2021
@Last Modified time: 19-07-2021
@Title : This Script provide method for CRUD operation in MySQL Database.
'''


import mysql.connector
from log import logger

class CRUDMethods:

    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                        host = "localhost",
                        user = "root",
                        passwd = "",
                        )
            mycursor = self.db.cursor()
            mycursor.execute("CREATE DATABASE DB1")
            print("DB Created")             
        except Exception as ex:
            logger.error(ex) 


    #def DBCreation(self):
     #   try:
      #      cursorObject = self.database.cursor()
       #     cursorObject.execute("CREATE DATABASE DB1")
        #    print("DB Created")       
        #except Exception as ex:
         #   logger.error(ex)

    def TableCreation(self):
        try:
            studentRecord = """CREATE TABLE STUDENT (
                   NAME  VARCHAR(20) NOT NULL,
                   BRANCH VARCHAR(50),
                   ROLL INT NOT NULL,
                   SECTION VARCHAR(5),
                   AGE INT
                   )"""
            self.mycursor.execute(studentRecord)
            self.DB1.commit()
            self.print("Table Created")       
        except Exception as ex:
            logger.error(ex)


    def insertRecords(self):
        try:
            studentRecord = "INSERT INTO STUDENT(NAME,BRANCH,ROLL,SECTION,AGE) VALUES(%s,%s,%s,%s,%s)"
            val=[('Ram','CS',1,'A',22),('Shayam','EX',2,'B',24)]
            self.mycursor.executemany(studentRecord,val)
            self.db.commit()
            print("Records Inserted")       
        except Exception as ex:
            logger.error(ex)
    
    def updateRecords(self):
        '''
        Description:
            Method update records.
        Parameters:
            
        Return:
            
        '''
        try:
            studentsRecord = "UPDATE STUDENT SET NAME = 'SHIVAM' WHERE roll_no = 1"
            self.mycursor.execute(studentsRecord)
            self.db.commit()
            print("Records Updated") 
        except Exception as ex:
            logger.error(ex)
    
    def deleteRecords(self):
        try:
            studentsRecord = "DELETE FROM student WHERE ROLL = 2"
            self.mycursor.execute(studentsRecord)
            self.db.commit()
            print("Records Deleted") 
        except Exception as ex:
            logger.error(ex)
    
    def read_table(self):
        try:
            mycursor=self.db.cursor()
            mycursor.execute("SELECT * FROM STUDENT")
            rows=mycursor.fetchall()
            for row in rows:
                print(row)
        except Exception as ex:
            logger.error(ex)

    def sortRecords(self):
        try:
            studentsRecord = "SELECT * FROM STUDENT ORDER BY NAME"
            self.mycursor.execute(studentsRecord)
            self.db.commit()
            result = self.mycursor.fetchall()
            for x in result:
                print(x)
        except Exception as ex:
            logger.error(ex)

if __name__=="__main__":
    methods = CRUDMethods()

    #methods.DBCreation()
    methods.TableCreation()
    #methods.insertRecords()
    #methods.deleteRecords()
    #methods.updateRecords()
    #methods.sortRecords()
    #methods.read_table()
    