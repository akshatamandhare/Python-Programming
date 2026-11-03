## It helps to us to have the communication between python file and database

## There we use few function

##1. connect(): It is a function which helps to connect the python file with the database. The function is present in sqlite3 module
##2. cursor(): It helps the control to point to particular location
##3. execute(): It helps to write the queries
##4. commit(): It helps to save the changes we made
##5. close(): It helps to break the connection between python file and database

##################################################################################################

## Insertion

import sqlite3
# var = sqlite3.connect('EMPLOYEE.db')
# var1 = var.cursor()
# var1.execute('create table EMP_TABLE(EMP_NAME char, EMP_ID char)')
# var1.execute('insert into EMP_TABLE values("A", "TYP123")')
# var1.execute('insert into EMP_TABLE values("B", "TYP124")')
# var1.execute('insert into EMP_TABLE values("C", "TYP125")')
# var1.execute('insert into EMP_TABLE values("D", "TYP125")')
# var1.execute('insert into EMP_TABLE values("E", "TYP126")')
# var.commit()
# var.close()

#Extraction

# var = sqlite3.connect('EMPLOYEE.db')
# var1=var.cursor()
# res = var1.execute('select * from EMP_TABLE where EMP_NAME="A"')
# res1=res.fetchall()
# print(res1)
# var.commit()
# var.close()


#oracle database connection

import oracledb 

# Establish Oracle connection

import oracledb

try:
    # Establish Oracle connection
    conn = oracledb.connect(
        user="SCOTT",
        password="YOUR_PASSWORD",
        dsn="Akshata:1523/orclnew"
    )

    print("Oracle Database Connected Successfully!")

    # Create cursor
    cursor = conn.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM EMP")

    # Fetch records
    records = cursor.fetchall()

    # Display output
    for row in records:
        print(row)

    cursor.close()
    conn.close()

except oracledb.Error as e:
    print("Connection Error:", e)
