import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com")
contents = resp.text
bs = BeautifulSoup(contents, "html.parser")

schedule_table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
rows = schedule_table.find_all("tr")
for row in rows[1:]:
    title = row.find_all("td")[0].text
    timings = row.find_all("td")[1].text
    stdate = row.find_all("td")[2].text
    print(f"{title:30} {stdate:10} {timings:15}")

    