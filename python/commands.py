import mysql.connector

connection = mysql.connector.connect(
    user='root', password='', host='mysql', port="3306" , database='abschlussprojekt')
print("Connected to abschlussprojekt")

cursor = connection.cursor()
cursor.execute("SELECT * FROM members")
members = cursor.fetchall()
connection.close()

print(members)
