class Animal:
    def comer(self):
        print('Comiendo')
    
    def pasear(self):
        print('Paseando animales')


class Perro:
    def pasear(self):
        print('Paseando al perro')

#Herencia multiple
class Canchito(Perro, Animal):
    def progrmar(self):
        print('programando')

chancho = Canchito()
chancho.pasear()