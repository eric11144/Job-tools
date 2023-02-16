#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import time
import pyodbc 

from pyModbusTCP.client import ModbusClient


HOST1 = "192.168.0.65"
PORT1 = 1502
c1 = ModbusClient()
c1.host(HOST1)
c1.port(PORT1)
c1.unit_id(1)
# now_epoch_time = now.timestamp()

# server = '127.0.0.1,1433' 
# database = 'Test' 
# username = 'SA' 
# password = 'p@55w0rd' 
# cnxn = pyodbc.connect(
#     '''
#     DRIVER={ODBC Driver 17 for SQL Server}; 
#     SERVER={server}; 
#     DATABASE={database}; 
#     UID={username}; 
#     PWD={password}
#     ''')
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=127.0.0.1,1433; DATABASE=Test; UID=SA; PWD=p@55w0rd')
cursor = cnxn.cursor()

# Get data from table
# cursor.execute("SELECT * FROM Inventory WHERE quantity > 140")
# rows = cursor.fetchall()
# for row in rows:
#     print(row.id, row.name, row.quantity)

# Creat table
sql_command = """
        CREATE TABLE Test
        (
            time datetime,
            Holding_40001 INT
        )
    """
try:
    cursor.execute(sql_command)
    cnxn.commit()
except pyodbc.ProgrammingError:
    print("Table 'Test' already exists.")

# Insert data to Database
while True:
    # open or reconnect TCP to server
    if not c1.is_open():
        if not c1.open():
            print("unable to connect to "+HOST1+":"+str(PORT1))

    if c1.is_open():
        # read 2 registers at address 0, store result in regs list
        regs = c1.read_holding_registers(0, 64)
        for i in range(63):
            now_string = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            data = regs[i] + regs[i+1]
            cursor.execute(
                """
                INSERT INTO Test
                (time, Holding_40001)
                VALUES (?, ?)
                """,
                (now_string, data)
            )
            cnxn.commit()

    # sleep 2s before next polling
    time.sleep(2)
