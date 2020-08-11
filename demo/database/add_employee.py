import sqlite3

con = sqlite3.connect(r"c:\classroom\july10\hr.db")
cur = con.cursor()
name = input("Enter  name :")
job = input("Enter job :")
salary = int(input("Enter salary :"))

try:
    cur.execute("insert into employees(name,job,salary) values(?,?,?)", (name, job, salary))
    con.commit()
    print("Added Employee Successfully!")
except Exception as ex:
    print("Sorry! Could not add employee due to error -->",ex)

con.close()
