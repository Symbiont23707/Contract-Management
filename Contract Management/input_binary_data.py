import mysql.connector

my_connect = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Mghfghmghfgh4573434",
    database="contract",
)
my_cursor = my_connect.cursor()

path = "2.png"

with open(path,"rb") as file:
    BinaryData = file.read()
    SQLStatement = "INSERT INTO additional (image,id_info) VALUES (%s,%s);"
    my_cursor.execute(SQLStatement, (BinaryData, 1))
    my_connect.commit()
