# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
velocidad_asteroide = 49
advertencia = "CUIDADO EL ASTEROIDE SE ACERCA DEMASIADO RAPIDO!"
# Escribe una expresión de prueba para calcular si necesita una advertencia.
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.

if velocidad_asteroide > 25:
    print(advertencia)
else:
    print("No es nada, vete a dormir")


velocidad_asteroide = 19
advertencia = "TODO MUNDO BUSQUE UN ASTEROIDE EN EL CIELO"

if velocidad_asteroide > 20:
    print(advertencia)
elif velocidad_asteroide == 20:
    print(advertencia)
else:
    print("NADIE BUSQUE NADA")
