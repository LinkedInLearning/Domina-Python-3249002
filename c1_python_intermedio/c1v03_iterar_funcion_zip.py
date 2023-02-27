lista_nombres = ["Ana", "Paco", "Javier", "Emilio"]
lista_edades = [25, 27, 25, 26]

datos_zip = zip(lista_nombres, lista_edades)
print(datos_zip)

print(list(datos_zip))

for nombre, edad in datos_zip:
    print(nombre, edad)
