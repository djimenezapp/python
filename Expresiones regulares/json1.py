import json
producto1={"nombre":"silla", "color":"blanco", "precio":80}

resultado=json.dumps(producto1)
resultado2= json.loads(resultado)
print(resultado2)