import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.khanacademy.org/")
contents = resp.text
bs = BeautifulSoup(contents, "html.parser")

for tag in bs.find_all("a"):
    print(tag['href'])

print('Done!')