import mysql.connector
from mysql.connector import Error

def crear_tabla(bbdd):
    try:
        connection=mysql.connector.connect(host='localhost',database='cumpleaños',user='root',password='root')

        query="""
        Create table cumpleaño(
	Id int(11) not null,
    Name varchar(250) not null,
    fecha Date not null,
    primary key (Id))
        """
        result=cursor.execute(query)      

    except Error as e:
        print(e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("conexion cerrada")

def insertar_datos(data):
    try:
        connection=mysql.connector.connect(host='localhost',database='cumpleaños',user='root',password='root')
        cursor=connection.cursor()
        query="""
        Insert Into Values(%s,%s,%s)
        """
        result=cursor.executemany(query,data)
    except Error as e:
        print(e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("conexion cerrada")

datos=[(1,'Fabian','2006-04-05'),(2,'Roy','1998-06-19'),(3,'Rafa','2005-05-15'),(4,'Mar','2001-01-27')]
insertar_datos(datos)