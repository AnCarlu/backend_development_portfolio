#Definición de la clase
class Persona:

    def inicializar_persona(self, nombre, apellido):
        #Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido= apellido

    def mostrar_contacto(self):
        print(f'''Persona:
            Nombre: {self.nombre}
            Apellido: {self.apellido}''')
        
    
#Creación de objeto
if __name__=='__main__': #Creación de la condición para que solo se ejecute este código desde este archivo
    #Creación de un primer objeto
    persona1 = Persona() #Crea un objeto vacio en memoria
    persona1.inicializar_persona('Layla','Acosta')
    persona1.mostrar_contacto()

    #Creacion segundo objeto

    persona2= Persona()
    persona2.inicializar_persona('Ian','Sanchez')
    print(persona2.mostrar_contacto())
    

