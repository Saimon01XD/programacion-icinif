ciudades = ["Santiago", "Temuco", "Osorno", "Punta Arenas"]
indice_de_calidad = [134, 99, 245, 50]

conjunto = ciudades + indice_de_calidad
mejor_calidad = min(indice_de_calidad)
peor_calidad = max(indice_de_calidad)

print(f"La ciudad de {ciudades[3]} tiene el mejor indice de calidad del aire con: {mejor_calidad}")

if 0 < (mejor_calidad <= 50):
    print(f"{ciudades[3]}: Buena calidad del aire")

if 51 <= (mejor_calidad <= 100):
    print(f"{ciudades[3]}: Calidad del aire moderada")

if 101 <= (mejor_calidad <= 150):
    print(f"{ciudades[3]}: Calidad del aire dañina a la salud para grupos sensibles")

if 151 <= (mejor_calidad <= 200):
    print(f"{ciudades[3]}: Calidad del aire dañina para la salud")

if 201 <= (mejor_calidad < 300):
    print(f"{ciudades[3]}: Calidad del aire muy dañina para la salud")

if 300 <= mejor_calidad :
    print(f"{ciudades[3]}: Calidad del aire peligrosa")

####

print(f"La ciudad de {ciudades[2]} tiene el peor indice de calidad del aire con: {peor_calidad}")

if 0 < (peor_calidad <= 50):
    print(f"{ciudades[2]}: Buena calidad del aire")

if 51 <= (peor_calidad <= 100):
    print(f"{ciudades[2]}: Calidad del aire moderada")

if 101 <= (peor_calidad <= 150):
    print(f"{ciudades[2]}: Calidad del aire dañina a la salud para grupos sensibles")

if 151 <= (peor_calidad <= 200):
    print(f"{ciudades[2]}: Calidad del aire dañina para la salud")

if 201 <= peor_calidad < 300:
    print(f"{ciudades[2]}: Calidad del aire muy dañina para la salud")

if 300 <= peor_calidad :
    print(f"{ciudades[2]}: Calidad del aire peligrosa")


