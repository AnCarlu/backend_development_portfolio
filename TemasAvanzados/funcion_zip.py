nombre =['Adrian','Juan','Maria']
edad=[30,25,35]
ciudad= ['Madrid','Barcelona','Sevilla']

#Combinar los elementos correspondientes usando la función zip
personas=zip(nombre, edad, ciudad)

#Iterar sobre el resultado de la función zip
for persona in personas:
    print(persona)