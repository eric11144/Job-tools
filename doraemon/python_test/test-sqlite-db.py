#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')

print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
       (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
        NAME           TEXT         NOT NULL,
        AGE            INTEGER      NOT NULL);
        ''')

conn.execute('''CREATE TABLE PERSON
    ( ID    INTEGER     NOT NULL,
      ORD   INTEGER,
      FOREIGN KEY (ID) REFERENCES COMPANY(ID));
    ''')

conn.execute('''CREATE TABLE PER
    ( ID    INTEGER     NOT NULL,
      ORD   INTEGER,
      FOREIGN KEY (ID) REFERENCES COMPANY(ID));
    ''')

conn.execute('''CREATE TABLE ser
    ( ID    INTEGER     NOT NULL,
      ORD   INTEGER,
      FOREIGN KEY (ID) REFERENCES COMPANY(ID));
    ''')

print ("Table created successfully")


conn.execute("PRAGMA foreign_keys = on")

conn.execute("INSERT INTO COMPANY (NAME,AGE)" \
      "VALUES ('Paul', 32 )");

conn.execute("INSERT INTO PERSON (ID,ORD)" \
      "VALUES ((SELECT ID from COMPANY WHERE COMPANY.NAME = 'Paul'), 88)");

conn.execute("INSERT INTO PER (ID,ORD)" \
      "VALUES ((SELECT ID from COMPANY WHERE COMPANY.NAME = 'Paul'), 88)");

conn.execute("INSERT INTO ser (ID,ORD)" \
      "VALUES ((SELECT ID from COMPANY WHERE COMPANY.NAME = 'Paul'), 88)");

conn.commit()
print ("Records created successfully")

# cursor = conn.execute("SELECT id, name, age  from COMPANY")
# for row in cursor:
#     print ("ID = ", row[0])
#     print ("NAME = ", row[1])
#     print ("AGE = ", row[2] ,"\n")

# cursor = conn.execute("SELECT id, ord from PERSON")
# for row_1 in cursor:
#     print ("ID = ", row_1[0])
#     print ("ORD = ", row_1[1],"\n")

# print()

cursor = conn.execute("SELECT c.age, p.ord FROM COMPANY c INNER JOIN PERSON p")
print(cursor.fetchall())

print ("Operation done successfully")

conn.close()
