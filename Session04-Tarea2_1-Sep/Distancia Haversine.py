import math
lat1 = float(input("Ingrese la latitud del primer punto en grados: "))
lon1 = float(input("Ingrese la longitud del primer punto en grados: "))

lat2 = float(input("Ingrese la latitud del segundo punto en grados: "))
lon2 = float(input("Ingrese la longitud del segundo punto en grados: "))

lat1_rad = math.radians(lat1)
lon1_rad = math.radians(lon1)
lat2_rad = math.radians(lat2)
lon2_rad = math.radians(lon2)

radioTierra = 6371  

d = 2 * radioTierra * math.asin(math.sqrt(math.sin((lat2_rad - lat1_rad) / 2)**2
 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin((lon2_rad - lon1_rad) / 2)**2))

print("La distancia es: ", round(d, 3), " km")