#Función cuadrado sin usar lambda
def cuadrado(x):
    return x **2

print(f"El cuadrado de 5 es : {cuadrado(5)}")

#Función lambda (anónima)

cuadrado_lambda = lambda x : x ** 2

print(f'El cuadrado de 16 es: {cuadrado_lambda(16)}')