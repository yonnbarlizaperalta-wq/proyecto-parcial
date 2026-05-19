from country_api import CountryAPI


def main():
    api = CountryAPI()


if __name__ == "__main__":
    main()

    names = ["colombia", "peru", "germany", "canada"]

    countries = api.by_names(names)

    for c in countries:
        print(c)

    if len(countries) > 1:
        base = countries[0]
        otros = countries[1:]

        base.comparar(otros)

if __name__ == "__main__":
    main()