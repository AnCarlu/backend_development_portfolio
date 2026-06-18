#Abrir un archivo en modo exclusivo

nombre_archivo= 'miarchivo.txt'

try:
    with open(nombre_archivo, 'x') as archivo:
        archivo.write('Escritura en modo exclusivo \n')
        archivo.write('Esperando que sea útil \n')
    print(f'Se ha creado el archivo {nombre_archivo}')
except FileExistsError as e:
    print(f'El archivo {nombre_archivo} ya existe')
    print(f'Detalle del error: {e}')