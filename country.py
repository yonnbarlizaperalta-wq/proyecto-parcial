class Country:
    def __init__(self, data: dict):
        self.nombre = data.get("name", {}).get("common")

        capitales = data.get("capital")
        self.capital = capitales[0] if capitales else "N/A"

        self.poblacion = data.get("population", 0)
        self.area = data.get("area", 0)
        self.region = data.get("region", "N/A")

    def __str__(self) -> str:
        return "Country"

    def density(self) -> float:
        return 0.0

    def comparar(self, otros: list):
        pass