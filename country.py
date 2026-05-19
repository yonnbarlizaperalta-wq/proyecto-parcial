class Country:
    def __init__(self, data: dict):
        self.nombre = data.get("name", {}).get("common")

        capitales = data.get("capital")
        self.capital = capitales[0] if capitales else "N/A"

        self.poblacion = data.get("poblacion", 0)
        self.area = data.get("area", 0)
        self.region = data.get("region", "N/A")

    def __str__(self) -> str:
        return "Country"

    def density(self) -> float:
        return 0.0

    def comparar(self, otros: list):
        pass
    
    def __str__(self) -> str:
        return f"{self.nombre} Capital: {self.capital}  Población: {self.poblacion}  Área: {self.area}"
    
    def density(self) -> float:
        if self.area == 0:
            return 0
        return self.poblacion / self.area
    
    def comparar(self, otros: list):
        todos = [self] + otros

    print("Pais | Poblacion | Area | Densidad")

    for p in todos: 
        print(p.nombre, p.poblacion, p.area, p.density())
        
    