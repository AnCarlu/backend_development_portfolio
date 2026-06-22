class Coordenadas:
    def __init__(self, lat, lon):
        self.lat= lat
        self.lon = lon
    
coords = Coordenadas(45,27)
coords2 = Coordenadas(45,27)

print(coords, coords2)