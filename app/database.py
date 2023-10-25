import mysql.connector

def connectorMysql():
    mydb = mysql.connector.connect(
            host="localhost",
            port = 3306,
            user="root",
            password="Anw175992587t+",
            database="simple_api"
    )
    return mydb