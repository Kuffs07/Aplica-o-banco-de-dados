import mysql.connector
from mysql.connector import Error


class DB:
    def __init__(self):
        host = 'Local instance MySQL80'
        database = 'Local instance MySQL80'
        user = 'root'
        password = 'xxxxx'
        try:
            self.__con = mysql.connector.connect(host=host, database=database, user=user, password=password)
            if self.__con.is_connected():
                db_info = self.__con.get_server_info()
                print(f'Conectado a DataBase! {db_info}')

        except Error as e:
            print(f'Acessar MySql: {e}')

    def ExecuteSQL(self, sql, select=False):
        try:
            cursor = self.__con.cursor()
            cursor.execute(sql)
            if not select:
                self.__con.commit()
            return cursor
        except Error as e:
            print('Error ao acessar a tabela', e)
            return False
