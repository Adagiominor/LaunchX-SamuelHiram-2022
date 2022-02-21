#3 aplicacion que captura nombres
from IPython.display import clear_output

new_planet = ''

planets = []

while new_planet.lower() != 'done':
    if(new_planet):
        planets.append(new_planet)
        print(planets)
    clear_output(wait=True)
    new_planet = input("introduce planetas -> ")


for planet in planets:
    print(planet)
