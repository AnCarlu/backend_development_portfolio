#Definición de la clase
class Coche:

    def __init__(self, marca, modelo,color):
        self.marca=marca #Atributo público
        self._modelo=modelo #Atributo protegido
        self.__color= color #Atributo privado

    def conducir(self):
        print(f'''Conduciendo el coche: 
        Marca: {self.marca} 
        Modelo: {self._modelo}
        Color: {self.__color}
        ''')
    
    #Metodo para leer el atributo
    def get_marca(self):
        return self.marca

    #Metodo para modificar el atributo
    def set_marca(self, marca):
        self.marca=marca
    
    #Metodo para leer el atributo
    def get_modelo(self):
        return self._modelo

    #Metodo para modificar el atributo
    def set_modelo(self, modelo):
        self._modelo=modelo
    
    #Metodo para leer el atributo
    def get_color(self):
        return self.__color

    #Metodo para modificar el atributo
    def set_color(self, color):
        self.__color=color

#Programa principal
if __name__ == '__main__':
    #Creación de un objeto
    coche1= Coche("Toyota", "Yaris", "Azul")
    coche1.conducir()
    #Desde aqui no se debe acceder a los atributos protegidos o privados
    #Aqui se utiliza la encapsulación, es decir los métodos get y set
    coche1.set_marca('Toyota 2')
    coche1.set_modelo ('Yaris 2')
    coche1.set_color('Azul 2')
    coche1.conducir()