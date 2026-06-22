class Coordenadas:
    def __init__(self, lat, lon):
        self.lat= lat
        self.lon = lon

    ##Metodo magico para la comprobar igualdad de objetos
    def __eq__(self, value):
        return self.lat == value.lat and self.lon == value.lon
    
    ##Metodo magico para la comprobar la no igualdad de objetos
    def __ne__(self, value):
        return self.lat != value.lat or self.lon != value.lon
    
    #Metodo mágico para comprobar si es mayor que
    def __lt__(self, other):
        return self.lat + other.lat < self.lon + other.lon
    
    #Metodo mágico para comprobar si es menor que
    def __le__(self, other):
        return self.lat + other.lat <= self.lon + other.lon
    
coords = Coordenadas(45,27)
coords2 = Coordenadas(45,27)

print(coords != coords2)
print(coords < coords2)
print(coords <= coords2)