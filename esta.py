import random
import csv

def cargarEstaciones (): #estaciones seria el diccionario vacio al cual le voy a ir agregando las estaciones
	estaciones = {}
	archivoEstaciones = open("estaciones.csv","r",encoding = "utf-8")
	next(archivoEstaciones)
	lectorEstaciones = csv.reader(archivoEstaciones, skipinitialspace=True)
	for estacion in lectorEstaciones:
		for x in range(1,int(estacion[4])):		
			estaciones[int(estacion[3])] = {"Dirección": estacion[2] , "Latitud y longitud": (float(estacion[1]), float(estacion[0])) , "Capacidad": int(estacion[4]) , "Bicicletas": {} }
			for anclaje in range(1, estaciones[int(estacion[3])]["Capacidad"] + 1 ):
				estaciones[int(estacion[3])]["Bicicletas"][anclaje] = ""
	archivoEstaciones.close()
	return estaciones

def cargarBicicletas ():
	bicicletas = {}
	fin = ["",999999999]
	archivoBicicletas = open("bicicletas.csv","r", encoding = "utf-8")
	next(archivoBicicletas)
	bicicleta = leer(archivoBicicletas, fin)
	while int(bicicleta[1]) != fin[1]:
		bicicletas[int(bicicleta[1])] = ["En condiciones", "Anclada en estación"]
		bicicleta = leer(archivoBicicletas, fin)
	archivoBicicletas.close()
	return bicicletas

def repartirBicicletasEstacion (estaciones, bicicletas):
	lBicicletas = sorted(bicicletas.keys())
	bicisTotalesAsignadas = 0
	lBicisParaRepartir = []
	for estacion in estaciones:
		bicicletasRetiradas = random.randrange(7, estaciones[estacion]["Capacidad"] + 1)
		bicisTotalesAsignadas += bicicletasRetiradas
		lBicisParaRepartir += [bicicletasRetiradas]
	while bicisTotalesAsignadas != len(lBicicletas):
		lBicisParaRepartir.clear()
		bicisTotalesAsignadas = 0
		for estacion in estaciones:
			bicicletasRetiradas = random.randrange(7, estaciones[estacion]["Capacidad"] + 1)
			bicisTotalesAsignadas += bicicletasRetiradas
			lBicisParaRepartir += [bicicletasRetiradas]
	contador = 0
	for estacion in estaciones:
		anclaje = 1
		for x in range(lBicisParaRepartir[contador]):
			biciRetirada = random.choice(lBicicletas)
			estaciones [estacion]["Bicicletas"][anclaje] = biciRetirada
			anclaje += 1
			lBicicletas.remove(biciRetirada)
		contador += 1
	return estaciones, lBicicletas

def leer(archivo, fin):
	estacion = archivo.readline()
	lista = estacion.rstrip().split(",")
	return lista if estacion else fin

"""
estaciones, bicicletas = cargarEstaciones(), cargarBicicletas()
estaciones, bicis = repartirBicicletasEstacion(estaciones, bicicletas)

print(estaciones)
print(bicis) # esto es para que vean que queda vacia
"""