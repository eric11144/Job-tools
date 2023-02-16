#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import time
import pyodbc 

from pyModbusTCP.client import ModbusClient


HOST1 = "127.0.0.1"
PORT1 = 502
c1 = ModbusClient()
c1.host(HOST1)
c1.port(PORT1)
c1.unit_id(1)

# server = '127.0.0.1,1433' 
# database = 'Modbus' 
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
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=127.0.0.1,1433; DATABASE=Modbus; UID=SA; PWD=p@55w0rd')
cursor = cnxn.cursor()

# Creat table
sql_command = """
        CREATE TABLE Modbus
        (
            time datetime,
            Holding_40001 INT,
            Holding_40002 INT,
            Holding_40003 INT,
            coils_01 INT,
            coils_02 INT,
            coils_03 INT
        )
    """
try:
    cursor.execute(sql_command)
    cnxn.commit()
except pyodbc.ProgrammingError:
    print("Table 'Modbus' already exists.")

# Insert data to Database
while True:
    # open or reconnect TCP to server
    if not c1.is_open():
        if not c1.open():
            print("unable to connect to "+HOST1+":"+str(PORT1))

    if c1.is_open():
        # read 2 registers at address 0, store result in regs list
        regs = c1.read_holding_registers(0, 64)
        coils = c1.read_coils(0, 64)
        for i in range(20):
            now_string = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            data_0 = regs[i + 30] 
            data_1 = regs[i + 29] 
            data_2 = regs[i + 28] 
            coils_data_0 = coils[i]
            coils_data_1 = coils[i+1]
            coils_data_2 = coils[i+2]
            cursor.execute(
                """
                INSERT INTO Modbus
                (time, Holding_40001, Holding_40002, Holding_40003, coils_01, coils_02, coils_03)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (now_string, data_0, data_1, data_2, coils_data_0, coils_data_1, coils_data_2)
            )
            cnxn.commit()

    # sleep 2s before next polling
    time.sleep(1)
