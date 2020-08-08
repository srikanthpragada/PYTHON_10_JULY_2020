import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com")
contents = resp.text
bs = BeautifulSoup(contents, "html.parser")

for tag in bs.find_all("a"):
    print(tag['href'])
    