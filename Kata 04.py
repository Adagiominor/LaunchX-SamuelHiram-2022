text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""


parts = text.split('. ')

palabras_clave = ["average", "temperature", "distance"]

for oracion in parts:
    for palabra in palabras_clave:
        if(palabra in oracion):
            print(oracion)
            break

for oracion in parts:
    for palabra in palabras_clave:
        if(palabra in oracion):
            print(oracion.replace("C", "celcius"))
            break


## separas las oraciones, luego buscas en cada oracion alguna palabra clave, de tal forma que al ciclarlo y encontrar una clave imprimes




