#Funcion sum y next

lista = [1,2,3,4,5]

#Suma de todos los elementos
result= sum(lista)
print(f'Resultado de la suma {result}')

#Podemos proporcionar un valor inicial

resultado = sum(lista, 20)

print(f'Resultado de la suma con un valor inicial {resultado}')

#La función next
iterador = iter(lista)

#Con esta función se obtiene el próximo elemento del iterador
elemento = next(iterador)
print(f'Siguiente elemento del iterable : {elemento}')