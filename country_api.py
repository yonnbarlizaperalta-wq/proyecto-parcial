import requests
from country import Country


class CountryAPI:
    def __init__(self):
        self.base_url = "https://restcountries.com/v3.1"