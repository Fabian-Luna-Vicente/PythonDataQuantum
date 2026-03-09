import mysql.connector
from mysql.connector import Error

import pprint

def select():
    try:
        connector=mysql.connector.connect(host='localhost',database='Electronics',user='root',password='root') 
        select_query="select * from Laptop"
        cursor=connector.cursor(dictionary=True)
        cursor.execute(select_query)
        records=cursor.fetchall()

        for row in records:
            pprint.pprint(row)
            print()
    except Error as e:
        print(e)
    finally:
        if connector.is_connected():
            connector.close()
            cursor.close()
select()