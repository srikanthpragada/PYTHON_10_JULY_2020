import requests
from bs4 import BeautifulSoup
import re

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
contents = resp.text
bs = BeautifulSoup(contents, "xml")

items = bs.find_all("item")
for item in items:
    pubdate = item.pubDate.text
    if pubdate.find("2020") >= 0:
        title = re.sub(r"\s+", ' ',item.title.text).strip()
        print(title)






    