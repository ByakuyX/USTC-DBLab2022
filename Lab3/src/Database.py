# -*- coding: UTF-8 -*-
import MySQLdb

class Database():
    __db = None

    def __init__(self) -> None:
        pass

    def login(self, user, passwd, server_addr, dbname):
        try:
            self.__db = MySQLdb.connect(server_addr, user, passwd, dbname, charset = "utf8")
        except MySQLdb.Error as e:
            print(e)
            self.__db = None
    
    def execute(self, sql):
        try:
            cursor = self.__db.cursor()
            cursor.execute(sql)
            res = cursor.fetchall()
            self.__db.commit()
            return res
        
        except MySQLdb.Error as e:
            print(sql)
            print(e)
            self.__db.rollback()
            return None

    def isConnected(self):
        return self.__db is not None
