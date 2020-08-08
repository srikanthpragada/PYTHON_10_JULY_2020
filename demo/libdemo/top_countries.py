import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()

for c in sorted(countries, key=lambda c: c['population'], reverse=True)[:10]:
    print(f"{c['name']:50} {c['region']:15} {c['population']:10} ")
