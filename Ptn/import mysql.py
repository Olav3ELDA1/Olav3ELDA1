import mysql.connector
import datetime
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="elev",
    database="olav"
)
mycursor = mydb.cursor()
print("Connected..")
sql = "INSERT INTO sensor(verdi,tid) VALUES (%s,%s)"
verdi = 1.0
tid = datetime.datetime.now()

val = (verdi, tid)


mycursor.execute(sql, val)
mydb.commit()

print("Done")