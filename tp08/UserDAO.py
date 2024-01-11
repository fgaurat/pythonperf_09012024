import sqlite3
from User import User
from Singleton import Singleton

class UserDAO(metaclass=Singleton):

    def __init__(self,db_file) -> None:
        self.__con = sqlite3.connect("./tp08/formation.db")
    
    def __enter__(self):
        print('Starting')
        return self
    
    def __exit__(self, *exc):
        print('Finishing,',*exc)
        self.__con.close()
        return False    

    def findAll(self):
        sql = "SELECT * FROM `users_tbl`"
        cur= self.__con.cursor()
        res = cur.execute(sql)
        for d in res.fetchall():
            u = User(*d)
            yield u
    
    def __del__(self):
        print("def __del__(self)")
        self.__con.close()