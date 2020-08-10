import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
contents = resp.text
bs = BeautifulSoup(contents, "xml")

items = bs.find_all("item")
for item in items:
    pubdate = item.pubDate.text
    pdate = datetime.strptime(pubdate[5:16],"%d %b %Y")
    days = (datetime.now() - pdate).days
    if days <= 200:
        title = re.sub(r"\s+", ' ',item.title.text).strip()
        print(f"{days} day(s) ago - {title}")






    