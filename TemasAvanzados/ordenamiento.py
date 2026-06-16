print('*** Ordenamiento en Python***')

#sintaxis: sorted(iterable, key=None, reverse=False)

empleados= ['Juan', 'Adrián', 'Maria']
#Ordenar la lista
empleados_ordenados= sorted(empleados)

print(f'Empleados ordenados {empleados_ordenados}')

#Para ordenar de manera descendente
empleados_ordenados= sorted(empleados, reverse = True)
print(f'Empleados ordenados de manera descendente {empleados_ordenados}')

#Ordenar un diccionario
empleados_dict= [
    {'nombre': ' Juan', 'salario' : 3000},
    {'nombre': ' Maria', 'salario' : 2500},
    {'nombre': ' Adrian', 'salario' : 3500}
]

empleados_ordenados_salario= sorted(empleados_dict, key= lambda x : x['salario'])

print(f'Empleados ordenados por salario: {empleados_ordenados_salario}')