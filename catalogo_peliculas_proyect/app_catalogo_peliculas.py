from peliculas import Peliculas
from servicio_peliculas import ServiciosPeliculas


class AppCatalogoPeliculas:

    def __init__(self):
        self.servicio_peliculas=ServiciosPeliculas()
    
    def mostrar_menu(self):
        print('***App Catalogo Peliculas')
        while True:
            try:
                print(f'''Opciones:
                      1. Agregar pelicula
                      2. Listar peliculas
                      3. Eliminar catálogo de películas
                      4. Salir''')
                opcion=int(input('Escribe tu opción'))
                if opcion == 1:
                    nombre_pelicula = input('¿Cual es el nombre de la película?')
                    pelicula = Peliculas(nombre_pelicula)
                    self.servicio_peliculas.agregar_pelicula(pelicula)
                elif opcion == 2:
                    self.servicio_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicio_peliculas.eliminar_archivo_peliculas()
                elif opcion == 4:
                    print('Vuelve pronto')
                    break
                else: 
                    print('Opcion no valida\n')
            except ValueError:
                print("Error: introduce un número válido")
            except Exception as e:
                print('Ocurrio un error: {e}')

if __name__ == '__main__':
    app = AppCatalogoPeliculas()
    app.mostrar_menu()