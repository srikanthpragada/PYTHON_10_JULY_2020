import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()

for c in sorted(countries, key=lambda c: c['region']):
    print(f"{c['name']:50} {c['capital']:30} {c['region']}")
