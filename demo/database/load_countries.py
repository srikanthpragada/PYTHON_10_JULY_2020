import requests
import sqlite3

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()

con = sqlite3.connect(r"c:\classroom\july10\hr.db")
cur = con.cursor()
count = 0
for c in countries:
    cur.execute("insert into countries values(?,?,?)",
                (c['alpha3Code'], c['name'], c['population']))
    count += 1

con.commit()
con.close()
print(f"Loaded {count} countries!")
