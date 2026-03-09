import mysql.connector
from mysql.connector import Error

def crear_BBDD(bbdd):
    try:
        connection=mysql.connector.connect(host='localhost',database='Electronics',user='root',password='root')
        query=f"Create database if not exists {bbdd}"
        cursor=connection.cursor()
        result=cursor.execute(query)
        print("creado")

        query="""
        Create table Laptop(
	Id int(11) not null,
    Name varchar(250) not null,
    price float not null,
    puchase_date Date not null,
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

crear_BBDD("Electronics")