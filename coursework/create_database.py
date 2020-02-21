import random
import math
import sqlite3
import os

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = lowercase.upper()
numbers = '0123456789'
punctuation = '@_#*-&'

# returns an id using uniform probability for each character in the alphabet string
def getID() :
    id = ''
    alphabet = lowercase + uppercase + punctuation + numbers
    while (len(id) <= 5) :
        id += alphabet[random.randint(0,len(alphabet)-1)]
    return id

# return an arrival time using the uniform distribution between 0 and 100
def getArrival() :
    return random.uniform(0,100)

# return a duration rounded up to the next highest integer
def getDuration() :
    return math.ceil(random.expovariate(1))

# create an empty database with the heading formatting for the columns
def create_database(db_file):
    db = sqlite3.connect(db_file)
    cursor = db.cursor()

    c_1 = "Task INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL"
    c_2 = "ID TEXT NOT NULL"
    c_3 = "Arrival NUMERIC NOT NULL"
    c_4 = "Duration NUMERIC NOT NULL"

    sql_create_table = "CREATE TABLE SimulationData ({},{},{},{})".format(c_1,c_2,c_3,c_4)

    try:
        cursor.execute(sql_create_table)
    except sqlite3.OperationalError:
        print("{} already exists.".format(db_file))

    db.commit()
    cursor.close()

# insert using getID(), getArrival() and getDuration() for each of the 100 records
def insert_records(db_file):
    db = sqlite3.connect(db_file)
    cursor = db.cursor()

    for rowNumber in range(100):
        sql_insert = "INSERT INTO SimulationData(ID, \
        Arrival, Duration) VALUES ('{}','{}','{}')".format(getID(), getArrival(), getDuration())
        cursor.execute(sql_insert)

    db.commit()
    cursor.close()

# the file name
DB_FILE = "SimulationData.db"

# if the file name doesn't exist then create then create the database and insert the records.
if not os.path.exists(DB_FILE):
    create_database(DB_FILE)
    insert_records(DB_FILE)
