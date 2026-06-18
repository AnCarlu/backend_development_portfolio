#Creación de archivos

nombre_archivo= 'miarchivo.txt'

#Abrir archivo en modo escritura 

with open(nombre_archivo, 'w') as archivo:
    archivo.write('Hola como estas\n')
    archivo.write('Añadiendo información al archivo\n')


print(f'Se creó el archivo : {nombre_archivo}')