from datetime import *

def cargarViajesFinalizados (viajesFinalizados):
	fin = ["","","","","","", 9999999999999999]
	archivoViajes = open("viajes.csv","r", encoding = "utf-8")
	next(archivoViajes)
	viaje = leer(archivoViajes, fin)
	while int(viaje[6]) != fin[6]:
		horarioSalida = int(viaje[3][0:2]), int(viaje[3][3:5]), int(viaje[3][6:]) 
		horarioLlegada = int(viaje[5][0:2]), int(viaje[5][3:5]), int(viaje[5][6:])
		duracionViaje = int(viaje[4][0:2]), int(viaje[4][3:5]), int(viaje[4][6:])
		acumularViajes(int(viaje[2]), viajesFinalizados, int(viaje[6]), int(viaje[0]), int(viaje[1]), duracionViaje)
		#acumularViajes(int(viaje[2]), viajesFinalizados, int(viaje[6]), int(viaje[0]), int(viaje[1]), horarioSalida, horarioLlegada)
		viaje = leer(archivoViajes, fin)


def acumularViajes(usuario, viajesFinalizados, bicicletaAsignada, estacionRetirar, estacionDevolver, duracionViaje): #esta la saque del tp para guardar los viajes en el diccionario
	horaViaje, minutoViaje, segundoViaje = duracionViaje
	if usuario not in viajesFinalizados:
		viajesFinalizados[usuario] = [(bicicletaAsignada, estacionRetirar, estacionDevolver, time(horaViaje, minutoViaje, segundoViaje))]
	else:
		viajesFinalizados[usuario].append((bicicletaAsignada, estacionRetirar,  estacionDevolver,time(horaViaje, minutoViaje, segundoViaje) ))

def sumarViajes(viajesFinalizados):
	duraciones = {}
	for dni in viajesFinalizados:
		duracionDias = 0
		duracionHora = 0
		duracionMin = 0
		duracionSeg = 0
		for viaje in range(len(viajesFinalizados[dni])):
			duracionHora += viajesFinalizados[dni][viaje][3].hour
			duracionMin += viajesFinalizados[dni][viaje][3].minute
			duracionSeg += viajesFinalizados[dni][viaje][3].second
		if duracionSeg >= 60:
			diferencia1 = duracionSeg // 60
			sumar1 = duracionSeg % 60
			duracionMin += diferencia1
			duracionSeg = sumar1
		if duracionMin >= 60:
			diferencia2 = duracionMin // 60
			sumar2 = duracionMin % 60
			duracionHora += diferencia2
			duracionMin = sumar2
		if duracionHora >= 24:
			diferencia3 = duracionHora // 24
			sumar3 = duracionHora % 24
			duracionDias += diferencia3
			duracionHora = sumar3
		duraciones[dni] = [ duracionDias, time(duracionHora, duracionMin, duracionSeg)]
	topOrdenado = sorted(duraciones.items(), key = lambda x: x[1], reverse = True)
	contador = 1
	for usuarios in topOrdenado[0:5]:
		print(contador,"El usuario {} con {} dias y {} hs de viaje.".format(usuarios[0], usuarios[1][0], usuarios[1][1]))
		contador +=1

def leer(archivo, fin):
	linea = archivo.readline()
	lista = linea.rstrip().split(",")
	return lista if linea else fin
