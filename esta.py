import random

def cargarEstaciones (): #estaciones seria el diccionario vacio al cual le voy a ir agregando las estaciones
	estaciones = {}
	fin = ["","","","9999999999999",""]
	archEstaciones = open("estaciones.csv","r",encoding = "utf-8")
	next(archEstaciones)
	estacion = leer(archEstaciones, fin)
	
	while estacion[3] != fin[3]:
		for x in range(1,int(estacion[4])):
			if estacion[2].endswith('"'):
				estacion[2] = estacion[2][1 : (len(estacion[2])-1)]
			estaciones[int(estacion[3])] = {"Dirección": estacion[2] , "Latitud y longitud": (float(estacion[1]), float(estacion[0])) , "Capacidad": int(estacion[4]) , "Bicicletas": [] }
			for anclaje in range(1, estaciones[int(estacion[3])]["Capacidad"] + 1 ):
				estaciones[int(estacion[3])]["Bicicletas"].append([anclaje, ""])
		estacion = leer(archEstaciones,fin)

		#longitud, latitud, direccion, identificador, capacidad
		#identificador, direcciones, latitudLongitud, anclajesTotales, anclajesOcupados
	
	archEstaciones.close()
	return estaciones

def cargarBicicletas ():
	bicicletas = {}
	fin = ["","999999999"]
	archBicis = open("bicicletas.csv","r", encoding = "utf-8")
	next(archBicis)
	bicicleta = leer(archBicis, fin)
	while bicicleta[1] != fin[1]:
		bicicletas[bicicleta[1]] = ["En condiciones", "Anclada en estación"]
		bicicleta = leer(archBicis, fin)
	archBicis.close()
	return bicicletas

def repartirBicicletasEstacion (estaciones, bicicletas):
	lBicis = sorted(bicicletas.keys())
	for estacion in range(1, len(estaciones) + 1 ):
		bicisRetiradas = random.randrange(15,estaciones[estacion]["Capacidad"])
		anclaje = 0
		for x in range (bicisRetiradas):
			biciRetirada = random.choice(lBicis)
			estaciones [estacion]["Bicicletas"][anclaje][1] = biciRetirada
			anclaje += 1
			lBicis.remove(biciRetirada)
	return estaciones

def leer(archivo, fin):
	linea = archivo.readline()
	lista = linea.rstrip().split(",")
	return lista if linea else fin

estaciones, bicicletas = cargarEstaciones(), cargarBicicletas()

print (estaciones)
print(bicicletas)

estaciones = repartirBicicletasEstacion(estaciones, bicicletas)

print(estaciones)
