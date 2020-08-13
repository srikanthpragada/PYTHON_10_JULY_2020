# Summary of employees

import sqlite3

con = sqlite3.connect(r"c:\classroom\july10\hr.db")
cur = con.cursor()
cur.execute("select  count(id), avg(salary), min(salary), max(salary) from employees")
row = cur.fetchone()
con.close()

print(f"No. of employees : {row[0]:10}")
print(f"Average Salary   : {row[1]:10.0f}")
print(f"Minimum Salary   : {row[2]:10}")
print(f"Maximum Salary   : {row[3]:10}")
