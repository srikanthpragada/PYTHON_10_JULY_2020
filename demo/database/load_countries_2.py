import requests
import sqlite3

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()

con = sqlite3.connect(r"c:\classroom\july10\hr.db")
cur = con.cursor()
rows = []
for c in countries:
    rows.append((c['alpha3Code'], c['name'], c['population']))

cur.executemany("insert into countries values(?,?,?)",rows)
print(f"Loaded {len(rows)} countries!")
con.commit()
con.close()

