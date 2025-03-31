import re

texto="Hola, mi nombre es antonio"
resultado=re.search("antonio$", texto)
resultado=re.search("antonio$", texto)
resultado=re.search("mi.*es", texto)

if(resultado):
    print("Cadena encontrada")
else:
    print("Cadena no encontrada")
texto1="""
El coche de Luis es rojo,
el coche de antonio es blanco,
y el coche de maria es rojo
"""
resultado1=re.findall("coche.*rojo", texto1)

print(resultado1)
#split
texto2="La silla es blanca y vale 80"
resultado2=re.split("\s", texto2)
print(resultado2)
#sub
resultado3= re.sub("blanca","roja", texto2)
print(resultado3)