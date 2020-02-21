import csv
import sqlite3
import os
import calendar

def create_database(db_file):
    db = sqlite3.connect(db_file)
    cursor = db.cursor()

    c_1 = "transaction_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL"
    c_2 = "Organisation_Name TEXT NOT NULL"
    c_3 = "Purchase_Order_Number INTEGER NOT NULL"
    c_4 = "Order_Date INTEGER NOT NULL"
    c_5 = "Total_Value INTEGER NOT NULL"
    c_6 = "Supplier_Name TEXT NOT NULL"
    c_7 = "Account_Name TEXT NOT NULL"
    c_8 = "Service TEXT NOT NULL"

    sql_create_table = "CREATE TABLE PurchaseOrderTransactions ({},{},{},{},{},{},{},{})".format(c_1,c_2,c_3,c_4,c_5,c_6,c_7,c_8)

    try:
        cursor.execute(sql_create_table)
    except sqlite3.OperationalError:
        print("{} already exists.".format(db_file))

    db.commit()
    cursor.close()

def clean_currency(currency_string):
    return float(currency_string[1:].replace(",",""))

def insert_records(db_file, records):
    db = sqlite3.connnect(db_file)
    cursor = db.cursor()

    for row in records:
        row[3] = clean_currency(row[3])
        sql_insert = "INSERT INTO PurchaseOrderTransactions(Organisation_Name, \
        Purchase_Order_Number, Order_Date, Total_Value, Supplier_Name, \
        Account_Name, Service) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(*row)
        print(row)
        cursor.execute(sql_insert)

    db.commit()
    cursor.close()

def print_records(db_file):
    db = sqlite3.connect(db_file)
    cursor = db.cursor()

    sql_select = "SELECT * FROM PurchaseOrderTransactions"
    cursor.execute(sql_select)
    records=cursor.fetchall()

    for r in records:
        print(r)
    cursor.close()

def total_spent(db_file):
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    sql_query = "SELECT Total_Value FROM PurchaseOrderTransactions"

    total = 0
    for row in cursor.execute(sql_query):
        total += row[0]
    total = round(total, 2)
    print("Total spent : " + str(total))
    cursor.close()

def total_spent_by_month(db_file):
    db = sqlite3.connect(db_file)
    cursor = db.cursor()

    sql_query = "SELECT Order_Date,Total_Value FROM PurchaseOrderTransactions"

    result_dict = {}
    for row in cursor.execute(sql_query):
        date = row[0].split("/")
        month = calendar.month_name[int(date[1])]
        year = date[2]
        amount = row[1]
        key = month + " " + Year
        if key in result_dict:
            result_dict[key] += amount
        else:
            result_dict[key] = amount

    for k,v in result_dict.items():
        print(k + " : " + str(round(v,2)))

    cursor.close()

def add_transaction(db_file):
    db = sqlite3.connect(db_file)
    cursor = db.cursor()

    row = []
    row.append(input("Organisation Name: "))
    row.append(input("Purchase Order Number: "))
    row.append(input("Order Date (dd/mm/yyyy): "))
    row.append(input("Total Value (number): "))
    row.append(input("Supplier Name: "))
    row.append(input("Account Name: "))
    row.append(input("Service: "))
    sql_insert = "INSERT INTO PurchaseOrderTransactions(Organisation_Name, \
    Purchase_Order_Number, Order_Date, Total_Value, Supplier_Name, \
    Account_Name, Service) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(*row)
    cursor.execute(sql_insert)
    db.commit()
    cursor.close()

def delete_transaction(db_file, ID):
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    cursor.execute("DELETE FROM PurchaseOrderTransactions WHERE Transaction_id="+str(ID))
    db.commit()
    cursor.close()

DB_FILE = "PurchaseOrderTransactions.db"

csv_file = "purchase-orders.csv"
with open(csv_file) as f:
    reader = csv.reader(f)
    DATA = [line for line in reader][1:]

if not os.path.exists(DB_FILE):
    create_database(DB_FILE)
    insert_records(DB_FILE, DATA)

total_spent(DB_FILE)
total_spent_by_month(DB_FILE)

delete_transaction(DB_FILE, 1)
add_transaction(DB_FILE)

print_records(DB_FILE)
