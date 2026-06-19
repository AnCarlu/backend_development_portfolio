from servicio_snacks import ServicioSnacks
from snack import Snack


class MaquinaSnacks:
    def __init__(self):
        self.servicio_snacks = ServicioSnacks()
        self.productos= []

    def maquina_snacks(self):
        salir=False
        print('***Maquina de Snacks***')
        #Muestra el catalogo inicial al encender la máquina
        self.servicio_snacks.mostrar_snacks()
        #Bucle principal de la app
        #Mientras no se elija la opcion de salir el programa seguira ejecutandose
        while not salir:
            try:
                opcion= self.mostrar_menu()
                salir= self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Ocurrio un error: {e} ')

    #Menu principal de la aplicación
    def mostrar_menu(self):
        print(f'''Menu:
              1.Comprar snack
              2.Mostras ticket
              3.Agregar Nuevo Snack al inventario
              4.Inventario Snacks
              5.Salir''')
        #Convierte la entrada del usuario a un entero
        opcion = int(input('Elige una opción: '))
        return opcion
    
    #Metodo para derivar el flujo del programa
    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.servicio_snacks.mostrar_snacks()
        elif opcion == 5:
            print('Regresa pronto')
            return True #Devuelve True para acabar con el bucle while principal
        else:
            print(f'Opcion invalida : {opcion}')
            return False

    def comprar_snack(self):
        id_snack = int(input('¿Que snack quieres comprar?'))
        #Obtiene la lista actual de snacks del inventario
        snacks= self.servicio_snacks.get_snacks()
        #Busca el primer ID del snack que coincida con la entrada del usuario
        snack = next((snack for snack in snacks if snack.id_snack==id_snack), None)
        if snack:
            self.productos.append(snack)
            print(f'Snack encontrado: {snack}')
        else:
            print(f'Id snack no encontrado: {id_snack}')
        
    
    def mostrar_ticket(self):
        if not self.productos:
            print('No hay snacks en el ticket')
            return
        #Suma de manera acumulativa los precios de cada snack que hay en el carrito
        total = sum(snack.precio for snack in self.productos)
        print("El ticket de venta:")
        for producto in self.productos:
            print(f'\t- {producto.nombre} - ${producto.precio:.2f}')
        print(f'\tTotal -> ${total:.2f}')

    #Captura los datos desde la consola para agregar un nuevo snack 
    def agregar_snack(self):
        nombre = input('Nombre del snack: ')
        precio = float(input('Precio del snack: '))
        #Crea la instancia y delega en la capa de servicio su inclusión en la lista
        nuevo_snack = Snack(nombre, precio)
        self.servicio_snacks.agregar_snack(nuevo_snack)
        print('Snack agregado correctamente')

#Programa principal
if __name__ == '__main__':
    maquina_snacks= MaquinaSnacks()
    maquina_snacks.maquina_snacks()