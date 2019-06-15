import random
from datetime import time

def topUsuariosCantidadViajes(usuarios, viajesFinalizados):
	top = {}
	for dni in viajesFinalizados:
		if len(top) <= 10:
			top[usuarios[dni][1]] = len(viajesFinalizados[dni])
	print("**** TOP 10 USUARIOS CON MAYOR CANTIDAD DE VIAJES ****")
	topOrdenado = sorted(top.items(), key = lambda x:x[1], reverse = True)
	for usuarios in topOrdenado:
		print("El usuario {} con {} viajes.".format(usuarios[0], usuarios[1]))

def topUsuariosDuracionViajes(viajesFinalizados):
	usuariosMasDuracion = {}
	for dni in viajesFinalizados:
		duracionHora = 0
		duracionMin = 0
		duracionSeg = 0
		for viaje in range(len(viajesFinalizados[dni])):
			salida = viajesFinalizados[dni][viaje][2]
			llegada = viajesFinalizados[dni][viaje][4]
			diferenciaHora = abs((llegada.hour - salida.hour))
			diferenciaMinutos = abs((llegada.minute - salida.minute))
			diferenciaSegundos = abs((llegada.second - salida.second))
			duracionHora += diferenciaHora
			duracionMin += diferenciaMinutos
			duracionSeg += diferenciaSegundos
			if duracionSeg >= 60:
				duracionMin += 1
				duracionSeg = duracionSeg - 60
			if duracionMin >= 60:
				duracionHora += 1
				duracionMin = duracionMin - 60
		duracion = time(duracionHora, duracionMin, duracionSeg)
		if dni not in usuariosMasDuracion:
			usuariosMasDuracion[dni] = duracion
		else:
			sumaSegundos = (usuariosMasDuracion[dni].second + duracion.second)
			if sumaSegundos >= 60:
				sumaMinutos = (usuariosMasDuracion[dni].minute + duracion.minute) + 1
				sumaSegundos = sumaSegundos - 60
			else:
				sumaMinutos = (usuariosMasDuracion[dni].minute + duracion.minute)
			if sumaMinutos >= 60:
				sumaHoras = (usuariosMasDuracion[dni].hour + duracion.hour)
				sumaMinutos = sumaMinutos - 60
			else: 
				sumaHoras = (usuariosMasDuracion[dni].hour + duracion.hour)
			usuariosMasDuracion[dni] = time(sumaHoras, sumaMinutos, sumaSegundos)
	print("\n**** USUARIOS CON MAYOR TIEMPO DE VIAJE ****\n")
	topOrdenado = sorted(usuariosMasDuracion.items(), key = lambda x: x[1], reverse = True)
	contador = 1
	for usuarios in topOrdenado:
		print(contador,"El usuario {} con {} hs de viaje.".format(usuarios[0], usuarios[1]))
		contador +=1

def bicicletasEnReparacion (bicicletas):
	bicisEnReparacion = []
	for bicicleta in bicicletas:
		if bicicletas[bicicleta][0] == "Necesita reparación":
			bicisEnReparacion.append(bicicleta)
	random.shuffle(bicisEnReparacion)
	print("\n**** DEPÓSITO DE BICICLETAS ****")
	for bicicleta in bicisEnReparacion:
		print("[INFO] La bicicleta {} necesita reparacion.".format(bicicleta))

def estacionesMasActivas(estaciones, viajesFinalizados):
	top = {}
	for dni in viajesFinalizados:
		for viajes in viajesFinalizados[dni]:
			if estaciones[viajesFinalizados[dni][viajesFinalizados[dni].index(viajes)][1]]["Dirección"] not in top:
				top[estaciones[viajesFinalizados[dni][viajesFinalizados[dni].index(viajes)][1]]["Dirección"]] = 1
			else:
				top[estaciones[viajesFinalizados[dni][viajesFinalizados[dni].index(viajes)][1]]["Dirección"]] += 1
			if estaciones[viajesFinalizados[dni][viajesFinalizados[dni].index(viajes)][3]]["Dirección"] not in top:
				top[estaciones[viajesFinalizados[dni][viajesFinalizados[dni].index(viajes)][3]]["Dirección"]] = 1
			else:
				top[estaciones[viajesFinalizados[dni][viajesFinalizados[dni].index(viajes)][3]]["Dirección"]] += 1
	print("\n**** ESTACIONES MÁS ACTIVAS ****")
	topOrdenado = sorted(top.items(), key = lambda x:x[1], reverse = True)
	for estaciones in topOrdenado:
		print("Estacion {} con {} retiros y devoluciones.".format(estaciones[0], estaciones[1]))