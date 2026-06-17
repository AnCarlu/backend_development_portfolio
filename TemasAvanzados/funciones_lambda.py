from functools import reduce

#Función cuadrado sin usar lambda
def cuadrado(x):
    return x **2

print(f"El cuadrado de 5 es : {cuadrado(5)}")

#Función lambda (anónima)

cuadrado_lambda = lambda x : x ** 2

print(f'El cuadrado de 16 es: {cuadrado_lambda(16)}')

#Con map y lambda se trabaja con valores iterables
numeros = [1,2,3,4,5]

#Aplicar la función lambda para obtener el cuadrado de cada numero
cuadrados= list(map(lambda x: x ** 2, numeros))

print(f'Resultado de usar map y lambda {cuadrados}')

#Con filter y lambda
pares= list(filter(lambda x : x % 2 == 0, numeros))

print(f'Resultado de usar filter para buscar los pares : {pares}')

# reduce y lambda
suma_iterativa = reduce(lambda x, y: x + y, numeros)

print(f'Suma acumulativa aplicando reduce: {suma_iterativa}')