import random
import csv

def cargarEstaciones (): #estaciones seria el diccionario vacio al cual le voy a ir agregando las estaciones
	estaciones = {}
	archivoEstaciones = open("estaciones.csv","r",encoding = "utf-8")
	next(archivoEstaciones)
	lectorEstaciones = csv.reader(archivoEstaciones, skipinitialspace=True)
	for estacion in lectorEstaciones:
		for x in range(1,int(estacion[4])):		
			estaciones[int(estacion[3])] = {"Dirección": estacion[2] , "Latitud y longitud": (float(estacion[1]), float(estacion[0])) , "Capacidad": int(estacion[4]) , "Bicicletas": [] }
			for anclaje in range(1, estaciones[int(estacion[3])]["Capacidad"] + 1 ):
				estaciones[int(estacion[3])]["Bicicletas"].append([anclaje, ""])

		#longitud, latitud, direccion, identificador, capacidad
		#identificador, direcciones, latitudLongitud, anclajesTotales, anclajesOcupados
	
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
	for estacion in estaciones:
		BicicletasRetiradas = random.randrange(7,estaciones[estacion]["Capacidad"])
		anclaje = 0
		for x in range(BicicletasRetiradas):
			biciRetirada = random.choice(lBicicletas)
			estaciones [estacion]["Bicicletas"][anclaje][1] = biciRetirada
			anclaje += 1
			lBicicletas.remove(biciRetirada)

	return estaciones

def leer(archivo, fin):
	estacion = archivo.readline()
	lista = estacion.rstrip().split(",")
	return lista if estacion else fin

estaciones, bicicletas = cargarEstaciones(), cargarBicicletas()
estaciones = repartirBicicletasEstacion(estaciones, bicicletas)

print(estaciones)
