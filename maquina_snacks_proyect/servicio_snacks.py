import os.path

from snack import Snack

class ServicioSnacks:
    #Atributo de clase para la persistencia
    nombre_archivo = 'snacks.txt'

    def __init__(self):
        #Lista en memoria para gestionar el inventario
        self.snacks = []

        #Revisa si ya existe el archivo de snacks
        #Si ya existe se obtienen los snacks del archivo
        if os.path.isfile(self.nombre_archivo):
            self.snacks = self.obtener_snacks()
        #Si no existe cargamos alguno snacks iniciales
        else:
            self.cargar_snacks_iniciales()

    def obtener_snacks(self):
        snacks = []
        try:
            #Abre el archivo en modo lectura
            with open(self.nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    id_snack, nombre, precio=linea.strip().split(',')
                    snack = Snack(nombre, float(precio))
                    snacks.append(snack)
        except Exception as e :
            print(f'Error al leer el archivo de snacks : {e}')
        return snacks

    #Catálogo de prodcutos por defecto si el prorama se ejecuta por primera vez
    def cargar_snacks_iniciales(self):
        snacks_iniciales= [
            Snack('Patatas', 70),
            Snack('Refresco', 50),
            Snack('Sandwich', 120)
        ]

        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)

    #Añade los snacks al final del archivo
    def guardar_snacks_archivo(self,snacks):
        try:
            with open(self.nombre_archivo, 'a') as archivo:
                for snack in snacks:
                    archivo.write(f'{snack.escribir_snack()}\n')
        except Exception as e:
            print(f'Error al guardar el snack en el archivo : {e}')

    #Añade un nuevo snack tanto a la lista en memoria como al archivo 
    def agregar_snack(self, snack):
        self.snacks.append(snack)
        self.guardar_snacks_archivo([snack])

    #Recorre e imprime cada objeto snack
    def mostrar_snacks(self):
        print('--Snacks en el inventario---')
        for snack in self.snacks:
            print(snack)

    #Método get para retornar la lista de snacks
    def get_snacks(self):
        return self.snacks