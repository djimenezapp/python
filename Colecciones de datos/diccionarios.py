diccionario_colores={"red":"rojo", "blue":"azul","yellow":"amarillo"}
print(diccionario_colores["red"])
diccionario_colores["black"]="negro"
for color in diccionario_colores:
    print(color)

diccionario_colores.pop("yellow")
del(diccionario_colores["black"])
print(diccionario_colores)

lista=[1,2,5,25,33,56,75,21,56,89,43,13,62,24]
numerob=21
if(numerob in lista):
    print("Si, esta en la lista")
else:
    print("No, no está en la lista")