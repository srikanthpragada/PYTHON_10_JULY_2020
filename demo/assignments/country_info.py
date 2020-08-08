import requests

code = input("Enter country code :")
resp = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")
if resp.status_code == 404:
    print("Sorry! Country not found!")
    exit()

country = resp.json()
for key, value in country.items():
    print(f"{key:20} - {value}")