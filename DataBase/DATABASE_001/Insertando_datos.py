import mysql.connector
from mysql.connector import Error

def insertar_datos():
    try:
        connection=mysql.connector.connect(host='localhost',database='Electronics',user='root',password='root')
        query="""
       Insert into laptop values(%s,%s,%s,%s)
        """
        cursor=connection.cursor()
        record=(("27","GAA",2000,'2020-10-10'),("25","AAF",2060,'2020-10-10'))
        result=cursor.executemany(query,record)
        connection.commit()
        print(cursor.rowcount)        
    except Error as e:
        print(e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("conexion cerrada")

insertar_datos()