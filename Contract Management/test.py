import mysql.connector

my_connect = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Mghfghmghfgh4573434",
    database="contract",
)
my_cursor = my_connect.cursor()

my_cursor.execute("select * from contract.additional where (id_info = 7)")
list_image = [image[1::] for image in my_cursor]
print(list_image)