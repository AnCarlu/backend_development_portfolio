#Dividir una cadena (función split)
cadena = 'Hola mundo'
palabras = cadena.split()
print(palabras)

#Buscar con find
posicion = cadena.find('mundo') 
print(f'Posicion de la cadena mundo: {posicion}')

#Reemplazar con replace
nueva_cadena= cadena.replace('mundo', 'amigo')
print(nueva_cadena)

#Multiplicación de cadenas
cadena = 'Hola '
resultado_multiplicacion_cadenas= cadena*3
print(f'Resultado multiplicción de cadenas: {resultado_multiplicacion_cadenas}')

#Limpiar con función strip

cadena = '    Hola mundo   '
cadena_limpia=cadena.strip()

print(cadena_limpia)