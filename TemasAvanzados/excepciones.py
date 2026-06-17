#Manejo de excepciones

def dividir(numerador, denominador):
    try:
       
        resultado = numerador/denominador
        print(f'Resultado de la división : {resultado}')
    except ZeroDivisionError:
        print(f'No es posible dividir entre 0')
    except TypeError:
        print("Los operandos deben ser numéricos")
    finally:
        print('Se termina de procesar las excepciones')

dividir(10,2)
dividir(10,0)
dividir(10, "5")


def dividir2(numerador, denominador):
    try:
         #Revisamos si el denominador es = 0
        if denominador == 0:
            raise Exception('El denominador es igual a 0')
        resultado = numerador/denominador
        print(f'Resultado de la división : {resultado}')
    except Exception as e:
        print(f'Ocurrió un error: {e}')
    
dividir2(10,2)
dividir2(10,0)