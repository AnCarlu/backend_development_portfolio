class Snack:
    #Atributo de clase
    #Funciona como contador global para generar IDs únicos
    contador_snacks = 0

    def __init__(self, nombre ='', precio= 0.0):
        #Se incrementa el contador global cada vez que se crea un nuevo snack
        Snack.contador_snacks += 1
        #Se asigna el valor del contador codo ID único
        self.id_snack = Snack.contador_snacks
        #Se guardan el nombre y precio en el atributo de instancia
        self.nombre= nombre
        self.precio = precio

    def __str__(self):
        return (f'Snack: id_snack = {self.id_snack}, nombre = {self.nombre},'
        f'precio = {self.precio}')
    
    def escribir_snack(self):
        return f'{self.id_snack},{self.nombre},{self.precio}'