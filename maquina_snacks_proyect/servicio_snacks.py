import os.path

from snack import Snack

class ServicioSnacks:
    nombre_archivo = 'snacks.txt'

    def __init__(self):
        self.snacks = []

        #Revisar si ya existe el archivo de snacks
        #Si ya existe se obtienen los snacks del archivo
        if os.path.isfile(self.nombre_archivo):
            self.snacks = self.obtener_snacks()
        #Si no existe cargamos alguno snacks iniciales
        else:
            self.cargar_snacks_iniciales()

    def obtener_snacks(self):
        snacks = []
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    id_snack, nombre, precio=linea.strip().split(',')
                    snack = Snack(nombre, float(precio))
                    snacks.append(snack)
        except Exception as e :
            print(f'Error al leer el archivo de snacks : {e}')
        return snacks

    def cargar_snacks_iniciales(self):
        snacks_iniciales= [
            Snack('Patatas', 70),
            Snack('Refresco', 50),
            Snack('Sandwich', 120)
        ]

        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)

    def guardar_snacks_archivo(self,snacks):
    
        try:
            with open(self.nombre_archivo, 'a') as archivo:
                for snack in snacks:
                    archivo.write(f'{snack.escribir_snack()}\n')
        except Exception as e:
            print(f'Error al guardar el snack en el archivo : {e}')

    def agregar_snack(self, snack):
        self.snacks.append(snack)
        self.guardar_snacks_archivo([snack])

    def mostrar_snacks(self):
        print('--Snacks en el inventario---')
        for snack in self.snacks:
            print(snack)

    def get_snacks(self):
        return self.snacks