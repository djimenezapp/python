#Listas
colores=["rojo","amarillo","verder"]
print(colores[1])
colores[0]="azul"
print(colores[0])
print(len(colores))
colores.append("naranja")
colores.remove("amarillo")
print(colores)
for color in colores:
    print(color)
colores.clear()
