import mysql.connector
from mysql.connector import Error


def connect():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='news_headlines',
                                             user='root',
                                             password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            # cursor.execute("select database();")
            # record = cursor.fetchone()
            # print("You're connected to database: ", record)
            cursor.execute("SELECT * FROM news")

            myresult = cursor.fetchall()
            print("Values: ", myresult)

    except Error as e:
        print("Error while connecting to MySQL", e)

    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

def close_connection(connection, cursor):
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


connect()