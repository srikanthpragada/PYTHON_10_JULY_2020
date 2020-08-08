import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")

countries_dict = {}
countries = resp.json()
for c in countries:
    countries_dict[c['alpha3Code']] = c

code = input("Enter 3 letters country code :")
if code not in countries_dict:
    print("Sorry! Country not found!")
    exit()

country = countries_dict[code]
# Get names of countries
names = []
for ccode in country["borders"]:
    name = countries_dict[ccode]["name"]
    names.append(name)

print("Name                        :", country["name"])
print("Countries sharing border    :", ",".join(names))




