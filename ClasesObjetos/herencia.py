class Animal:
    def comer(self):
        print('Comiendo')


class Perro(Animal):
    def pasear(self):
        print('Paseando')

perro = Perro() 
perro.comer()

#Herencia mutinivel, no debería hacerse más de 2 niveles
class Canchito(Perro):
    def progrmar(self):
        print('programando')

chancho = Canchito()
chancho.comer()