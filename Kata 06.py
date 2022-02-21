planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']

# Creamos la lista planets y la mostramos
for item in planets:
    print(item)

print(f"\nthere are {len(planets)} planets in the set planets.")

# Agregamos a plutón y mostramos el último elemento
planets.append('Pluto')

print(f"\nthere are {len(planets)} planets in the set planets. The last planet is {planets[-1]}")


##

user_planet = str(input("Please insert a planet --> ")).title()

index_planet = planets.index(user_planet)

if index_planet != -1:
    print(f"\nyour planet it's {str(user_planet).title()} and is the number {index_planet} at Solar System.")
    print(f"there is more nearby planets from Sun than {user_planet.title()} : {planets[0:index_planet]}.")
    print(f"there is more far planets from Sun than {user_planet.title()} : {planets[index_planet + 1:]}")
