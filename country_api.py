import requests
from country import Country
from concurrent.futures import ThreadPoolExecutor
class CountryAPI:
    def __init__(self):
        self.base_url = "https://restcountries.com/v3.1"
        def by_name(self, name: str):
            url = f"{self.base_url}/name/{name}"
            response = requests.get(url)
            if response.status_code != 200:
                 return None
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                 return Country(data[0])
            return None
    
    def by_region(self, region: str):
         url = f"{self.base_url}/region/{region}"
         response = requests.get(url)
         if response.status_code != 200:
              return []
         data = response.json()
         countries = []
         for item in data:
            countries.append(Country(item))
            return countries
         