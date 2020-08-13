# Convert Employees to JSON

import sqlite3
import json

con = sqlite3.connect(r"c:\classroom\july10\hr.db")
cur = con.cursor()
cur.execute("select * from employees")

employees = []

for emp in cur.fetchall():
    employee = {'id': emp[0], 'name': emp[1], 'job': emp[2], 'salary': emp[3]}
    employees.append(employee)

con.close()
# print(employees)

file = open("employees.json", "wt")
json.dump(employees, file)
file.close()
