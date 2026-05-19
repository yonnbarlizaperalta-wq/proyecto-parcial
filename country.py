class Country:
    def __init__(self, data: dict):
        self.nombre = data.get("name", {}).get("common")

        capitales = data.get("capital")
        self.capital = capitales[0] if capitales else "N/A"

        self.poblacion = data.get("population", 0)
        self.area = data.get("area", 0)
        self.region = data.get("region", "N/A")

    def __str__(self) -> str:
        return f"{self.nombre} Capital: {self.capital} Población: {self.poblacion} Área: {self.area}"

    def density(self) -> float:
        if self.area == 0:
            return 0
        return self.poblacion / self.area

    def comparar(self, otros: list):
        todos = [self] + otros

        print("Pais , Poblacion , Area , Densidad")

        for p in todos:
            print(f"{p.nombre} {p.poblacion} {p.area} {round(p.density(), 2)}")

        mayor_poblacion = todos[0]
        mayor_area = todos[0]
        mayor_densidad = todos[0]

        for p in todos:
            if p.poblacion > mayor_poblacion.poblacion:
                mayor_poblacion = p

            if p.area > mayor_area.area:
                mayor_area = p

            if p.density() > mayor_densidad.density():
                mayor_densidad = p

        print("\nResultados:")
        print("Mayor poblacion:", mayor_poblacion.nombre)
        print("Mayor area:", mayor_area.nombre)
        print("Mayor densidad:", mayor_densidad.nombre)