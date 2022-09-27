import mysql.connector
import sys
class Dbhelper:
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(host="localhost",user="root",password=""
        ,database="ht_df_demo")
            self.mycursor=self.conn.cursor()
        except:
            print("some error occured")
            sys.exit(0)

        else:
            print("connected to database")


    def register(self,name,email,password):
        try:
            self.mycursor.execute("""
            INSERT INTO `users` (`id`,`name`,`email`,`password`) VALUES (NULL,'{}','{}','{}');
            """.format(name,email,password))
            self.conn.commit()
        except:
             return -1
        else:
             return 1
    def search(self,email,password):
        self.mycursor.execute("""
        SELECT * FROM USERS WHERE email like "{}" AND password LIKE "{}"
        """.format(email,password))
        data=self.mycursor.fetchall()
        return data







