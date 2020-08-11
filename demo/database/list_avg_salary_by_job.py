# List employees from EMPLOYEES table

import sqlite3

con = sqlite3.connect(r"c:\classroom\july10\hr.db")
cur = con.cursor()
cur.execute("select job, avg(salary) from employees group by job order by 2")
for job in cur.fetchall():
    print(f"{job[0]:10} {job[1]:8}")

con.close()
