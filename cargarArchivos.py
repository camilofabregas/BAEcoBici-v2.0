from datetime import *
import pickle
import random
import csv

def cargarArchivos():
	usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados, robosBicicletas = dict(), dict(), dict(), dict(), dict(), dict()
	chequearUsuariosMaestro(usuarios)
	cargarEstaciones(estaciones)
	cargarBicicletas(bicicletas)
	cargarRobosBicicletas(robosBicicletas)
	repartirBicicletasEstacion(estaciones, bicicletas)
	cargarViajesEnCurso(viajesEnCurso)
	cargarViajesFinalizados (viajesFinalizados)
	return usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados, robosBicicletas

def chequearUsuariosMaestro(usuarios):
	try:
		archUsuariosMaestro = open("usuariosMaestro.csv", "r")
		print("\n\n\n [INFO] No se han unificado los usuarios ya que un archivo maestro fue encontrado en el sistema.")
	except FileNotFoundError:
		archUsuariosMaestro = unificarUsuarios()
		print("\n\n\n [INFO] Se han detectado 4 archivos de usuarios, los cuales fueron mezclados por DNI en un único archivo maestro.")
	cargarUsuarios(usuarios, archUsuariosMaestro)

def unificarUsuarios():
	fin = ["", "", 9999999999999999, ""]
	usuarios = open("usuariosMaestro.csv", "w+") # Lo creo, ya que no existe
	usuarios1 = open("usuarios1.csv", "r")
	usuarios2 = open("usuarios2.csv", "r")
	usuarios3 = open("usuarios3.csv", "r")
	usuarios4 = open("usuarios4.csv", "r")
	next(usuarios1)
	next(usuarios2)
	next(usuarios3)
	next(usuarios4)
	listaU1 = leer(usuarios1, fin)
	listaU2 = leer(usuarios2, fin)
	listaU3 = leer(usuarios3, fin)
	listaU4 = leer(usuarios4, fin)
	while int(listaU1[2]) != fin[2] or int(listaU2[2]) != fin[2] or int(listaU3[2]) != fin[2] or int(listaU4[2]) != fin[2]:
		menor = min(int(listaU1[2]), int(listaU2[2]), int(listaU3[2]), int(listaU4[2]))
		if menor == int(listaU1[2]):
			usuarios.write("{},{},{},{}\n".format(listaU1[0], listaU1[1], listaU1[2], listaU1[3]))
			listaU1 = leer(usuarios1, fin)
		elif menor == int(listaU2[2]):
			usuarios.write("{},{},{},{}\n".format(listaU2[0], listaU2[1], listaU2[2], listaU2[3]))
			listaU2 = leer(usuarios2, fin)
		elif menor == int(listaU3[2]):
			usuarios.write("{},{},{},{}\n".format(listaU3[0], listaU3[1], listaU3[2], listaU3[3]))
			listaU3 = leer(usuarios3, fin)
		elif menor == int(listaU4[2]):
			usuarios.write("{},{},{},{}\n".format(listaU4[0], listaU4[1], listaU4[2], listaU4[3]))
			listaU4 = leer(usuarios4, fin)
	usuarios1.close()
	usuarios2.close()
	usuarios3.close()
	usuarios4.close()
	usuarios.seek(0,0)
	return usuarios

def cargarUsuarios(usuarios, archUsuariosMaestro):
	fin = ["", "", 9999999999999999, ""]
	usuario = leer(archUsuariosMaestro, fin)
	while int(usuario[2]) != fin[2]:
		usuarios[int(usuario[2])] = [usuario[3], usuario[0].lower().replace(" ", "_"), usuario[1]]
		usuario = leer(archUsuariosMaestro, fin)

def cargarEstaciones(estaciones):
	archivoEstaciones = open("estaciones.csv","r",encoding = "utf-8")
	next(archivoEstaciones)
	lectorEstaciones = csv.reader(archivoEstaciones, skipinitialspace=True)
	for estacion in lectorEstaciones:
		for x in range(1,int(estacion[4])):		
			estaciones[int(estacion[3])] = {"Dirección": estacion[2] , "Latitud y longitud": (float(estacion[1]), float(estacion[0])) , "Capacidad": int(estacion[4]) , "Bicicletas": {} }
			for anclaje in range(1, estaciones[int(estacion[3])]["Capacidad"] + 1 ):
				estaciones[int(estacion[3])]["Bicicletas"][anclaje] = ""
	archivoEstaciones.close()

def cargarBicicletas(bicicletas):
	fin = ["",999999999]
	archivoBicicletas = open("bicicletas.csv","r", encoding = "utf-8")
	next(archivoBicicletas)
	bicicleta = leer(archivoBicicletas, fin)
	while int(bicicleta[1]) != fin[1]:
		bicicletas[int(bicicleta[1])] = ["En condiciones", "Anclada en estación"]
		bicicleta = leer(archivoBicicletas, fin)
	archivoBicicletas.close()

def repartirBicicletasEstacion(estaciones, bicicletas):
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

def cargarBinarios(ruta, robosBicicletas, viajesEnCurso):
	try:
		with open(ruta, 'rb') as arch:
			seguir = True
			while seguir:
				try:
					dato = pickle.load(arch)
					if ruta == 'viajesEnCurso.bin':
						viajesEnCurso[dato[0]] = [dato[1], dato[2], dato[3]]
					else:
						robosBicicletas[dato[0]] = [dato[1], dato[2]]
				except EOFError:
					seguir = False
			return viajesEnCurso, robosBicicletas
	except FileNotFoundError:
		return viajesEnCurso, robosBicicletas

def cargarViajesFinalizados (viajesFinalizados):
	fin = ["","","","","","", 9999999999999999]
	archivoViajes = open("viajes.csv","r", encoding = "utf-8")
	next(archivoViajes)
	viaje = leer(archivoViajes, fin)
	while int(viaje[6]) != fin[6]:
		horarioSalida = int(viaje[3][0:2]), int(viaje[3][3:5]), int(viaje[3][6:])
		horarioLlegada = int(viaje[5][0:2]), int(viaje[5][3:5]), int(viaje[5][6:])
		acumularViajes(int(viaje[2]), viajesFinalizados, int(viaje[6]), int(viaje[0]), int(viaje[1]), horarioSalida, horarioLlegada)
		viaje = leer(archivoViajes, fin)
	archivoViajes.close()

def acumularViajes(usuario, viajesFinalizados, bicicletaAsignada, estacionRetirar, estacionDevolver, horarioSalida, horarioLlegada):
	horaSalida, minSalida, segSalida = horarioSalida
	horaLlegada, minLlegada, segLlegada = horarioLlegada
	if usuario not in viajesFinalizados:
		viajesFinalizados[usuario] = [(bicicletaAsignada, estacionRetirar, time(horaSalida, minSalida, segSalida), estacionDevolver, time(horaLlegada, minLlegada, segLlegada))]
	else:
		viajesFinalizados[usuario].append((bicicletaAsignada, estacionRetirar, time(horaSalida, minSalida, segSalida), estacionDevolver, time(horaLlegada, minLlegada, segLlegada)))

def leer(archivo, fin):
	linea = archivo.readline()
	lista = linea.rstrip().split(",")
	return lista if linea else fin
