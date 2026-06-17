#Decoradores

def decorador(funcion):
    def wrapper(*args, **kwargs):
        print('Antes de llamar la función de saludar')
        result = funcion(*args,**kwargs) # Aqui se llama a nuestra función
        print('Despues de llamar la funcion saludar')
        return result
    return wrapper

@decorador
def saludar(nombre):
    print(f'Hola {nombre}')

saludar("Adrián")