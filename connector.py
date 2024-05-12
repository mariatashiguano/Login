# Login  verificacion de datos

import mysql.connector

class login_datos():

    def __init__(self):
        self.connector = mysql.connector.connect(
            host='localhost',
            database='loginpd',
            user='root',
            password='3050123540',
            port='3306'
        )

    def busca_users(self, users):
        cur = self.connector.cursor()
        sql = "SELECT * FROM login_datos WHERE Users = %s"
        cur.execute(sql, (users,))
        usersx = cur.fetchall()
        cur.close()
        return usersx 

    def busca_password(self, password):
        cur = self.connector.cursor()
        sql = "SELECT * FROM login_datos WHERE Password = %s"
        cur.execute(sql, (password,))
        passwordx = cur.fetchall()
        cur.close()
        return passwordx
