import requests
from country import Country


class CountryAPI:
    def __init__(self):
        self.base_url = "https://restcountries.com/v3.1"

    def by_name(self, name: str):
        url = f"{self.base_url}/name/{name}"

        response = requests.get(url)

        if response.status_code != 200:
            print("Error con:", name)   # 👈 IMPORTANTE PARA DEBUG
            return None

        data = response.json()

        # 👇 ESTO ES LA CLAVE
        if isinstance(data, list) and len(data) > 0:
            return Country(data[0])

        return None

    def by_names(self, names: list):
        countries = []

        for name in names:
            c = self.by_name(name)
            if c is not None:
                countries.append(c)

        return countries
                     