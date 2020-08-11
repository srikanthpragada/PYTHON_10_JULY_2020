import sqlite3

try:
    con = sqlite3.connect(r"c:\classroom\july10\hr.db")
    print("Connected to HR database!")
    con.close()
except Exception as ex:
    print("Error connecting to database :", ex)
