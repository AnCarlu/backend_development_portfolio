#Leer archivos en Python

nombre_archivo = 'miarchivo.txt'

#Leer archivos utilizando readlines
with open(nombre_archivo, 'r') as archivo:
    lineas=archivo.readlines()
    for linea in lineas:
        print(linea.strip())


#Leer todo el contenido usando el método read()
print('Leyendo el contenido con el método read')
with open(nombre_archivo, 'r') as archivo:
    print(archivo.read())