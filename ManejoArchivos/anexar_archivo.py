#Anexar información al archivo

nombre_archivo='miarchivo.txt'

with open(nombre_archivo, 'a') as archivo:
    archivo.write('Anexando información....\n')
    
    archivo.write('Saliendo de anexar información....\n')

print(f'Se ha anexado información al archivo: {nombre_archivo}')