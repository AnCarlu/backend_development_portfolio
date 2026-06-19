import os


class ServiciosPeliculas:

    def __init__(self):
        self.nombre_archivo= 'peliculas.txt'

    #Metodo para agregar películas
    def agregar_pelicula(self, pelicula):
        with open(self.nombre_archivo, 'a', encoding ='utf8') as archivo: #encoding ='utf8' permite agregar caracteres especiales
            archivo.write(f'{pelicula.nombre}\n')

    def listar_peliculas(self):
        with open(self.nombre_archivo, 'r', encoding ='utf8') as archivo:
            print('***Listado de peliculas***')
            print(archivo.read())

    def eliminar_archivo_peliculas(self):
        os.remove(self.nombre_archivo)
        print(f'El archivo {self.nombre_archivo} se ha eliminado correctamente')