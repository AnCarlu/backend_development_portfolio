class Perro:
    #Metodo mágico constructor
    def __init__(self, nombre):
        self.nombre = nombre

    #Metodo mágico destructor
    def __del__(self):
        print(f'Chao perrete {self.nombre}')
    
    def __str__(self):
        return f'Clase Perro:{self.nombre}'
    


perro = Perro('Corcho')
print(perro)
texto=str(perro)
print(texto)
del perro