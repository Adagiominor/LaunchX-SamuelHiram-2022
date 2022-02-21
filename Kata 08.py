planet = {
    'name':'mars',
    'moons': 2,
}

info = f"planet: {planet.get('name')}\nmoons: {planet['moons']}";

print(info)

planet['circunferencia (km)'] = {
    'polar': 6752,
    'equatorial': 6792,
}



print("\n" + info + f"\ncircunferencia (km): {planet['circunferencia (km)']['polar']}")



planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

planet = 0;

for value in planet_moons:
    planet = planet + 1;
print(f"planets: {planet}")

moons = 0;

for value in planet_moons.values():
    moons = moons + value;
print(f"total moons = {moons}")

prom = moons / planet 

print(f"promedio = {prom} ({moons}/{planet})")


# Añade el código para determinar el número de lunas.

# Obtenemos la lista de las lunas
# Almacenamos los resultados en una variable moons
moons = planet_moons.values()

print(moons)
# Obtenemos el total de planetas
# Almacenamos los resultados en una variable llamada years
planets = len(planet_moons.keys())

print(planets)
