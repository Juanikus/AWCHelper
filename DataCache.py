import sqlite3
from Resources import *

class DataCache:

    def __init__(self):
        self.dbCon = sqlite3.connect(DBNAME)
        self.__createTable()

    def __createTable(self):
        self.dbCon.execute("CREATE TABLE IF NOT EXISTS user (name text)")

    def getSavedUserName(self):
        userName = ''
        with self.dbCon:
            cursor = self.dbCon.cursor()
            resultSet = cursor.execute("SELECT name FROM user")
            row = resultSet.fetchone()
            if (row):
                userName = row[0]

        return userName

    def saveUserName(self, user):
        with self.dbCon:
            cursor = self.dbCon.cursor()
            param = (user,)
            cursor.execute("DELETE FROM user")
            cursor.execute("INSERT INTO user VALUES (?)", param)
