from ast import While
from msilib.schema import Error
import time
from Adafruit_IO import Client, Feed, RequestError
import pyfirmata
import mysql.connector
import datetime

run_count = 0
ADAFRUIT_IO_USERNAME = "Lust"
ADAFRUIT_IO_KEY = "aio_XgKh48jKA21683GDO14yiJoiDwrI"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

board = pyfirmata.Arduino('COM4')

it = pyfirmata.util.Iterator(board)
it.start()

digital_output = board.get_pin('d:12:o')

feed = Feed(name="counter")
# respose = aio.create_feed(feed)

# while True:
#     print('Sending count:', run_count)
#     aio.send_data('counter', run_count)
#     run_count += 1

#     time.sleep(5)


try:
    digital = aio.feeds('counter')
except RequestError:
    feed = Feed(name='Led')
    #digital = aio.create_feed(feed)

while True:
    print('Sending count:', run_count)
    run_count += 1
    aio.send_data('counter', run_count)

    data = aio.receive(digital.key)
    
    print('Data:', data.value)
    if data.value == "ON":
        digital_output.write(True)
    else:
        digital_output.write(False)

    time.sleep(3)

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
    time.sleep(15) #kjører koden og venter 15 sec for å kjøre den igjen så hvert 15 sec kjører koden og blir logget 

