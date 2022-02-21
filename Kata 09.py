from math import ceil

def function(tank1, tank2, tank3):
    return("Combustible en promedio en los 3 depositos: %s l" %prom(tank1,tank2,tank3))

def prom(num1, num2, num3):
    return(ceil((num1 + num2 + num3) / 3))

print(function(23.54,243.3,454.3))#litros





def inform(hora_lanzamiento, tiempo_vuelo, destino, tanque):
    return f"""
    Destino: {destino}
    Tiempo total: {hora_lanzamiento + tiempo_vuelo} minutes
    Combustible: {tanque} litros
    """

print(inform(destino="marte",hora_lanzamiento=30, tiempo_vuelo=20, tanque=300))

def informVar(destino,*minutos, **tanques):
    return f"""
    destino {destino}
    tiempo total: {sum(minutos)} minutos
    combustible: {sum(tanques.values())}

    """

print(informVar("mars", 23,424,535,636,34, principal=333, reserva=33))


def informVar(destino,*minutos, **tanques):
    repor = f"\ndestino {destino} \ntiempo total: {sum(minutos)} \nminutos \ncombustible: {sum(tanques.values())} l."
    for name, lts in tanques.items():
        repor += f"\n{name} -> {lts} l.";
    return repor

print(informVar('mars', 23, 44, 55, principal=3, secundario=23))
    
