import mysql.connector
from mysql.connector import Error

def actualizar_precio(id:int,precio:int):
    try:
        connector=mysql.connector.connect(host='localhost',user='root',database='Electronics',password='root')
        cursor=connector.cursor()
        query="update laptop set price= %s where id=%s"
        result=cursor.execute(query,(precio,id))
        connector.commit()
    except Error as e:
        print(e)
    finally:
        if connector.is_connected():
            connector.close()
            cursor.close()

actualizar_precio(27,2100)