import mysql.connector
from mysql.connector import Error

def buscar_precio(precio1:int,precio2:int):
    try:
        connector=mysql.connector.connect(host='localhost',user='root',database='Electronics',password='root')
        cursor=connector.cursor(dictionary=True)
        query="select * from Laptop where price between %s and %s"
        result=cursor.execute(query,(precio1,precio2))
        rows=cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)
    finally:
        if connector.is_connected():
            connector.close()
            cursor.close()

buscar_precio(2000,2100)