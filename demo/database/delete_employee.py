import sqlite3

try:
    con = sqlite3.connect(r"c:\classroom\july10\hr.db")
    cur = con.cursor()
    id = int(input("Enter employee id :"))
    try:
      cur.execute("delete from employees where empid = ?", (id,))
      if cur.rowcount == 1:  # no. of rows updated
        print("Deleted Employee Successfully!")
        con.commit()
      else:
        print("Sorry! Employee id not found!")
    except Exception as ex:
        print("Error while deleting employee :", ex)

except Exception as ex:
    print("Error : ", ex)

con.close()
