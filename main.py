from country_api import CountryAPI


def main():
    api = CountryAPI()


if __name__ == "__main__":
    main()

    names = ["colombia", "peru", "germany", "canada"]

    countries = api.by_names(names)