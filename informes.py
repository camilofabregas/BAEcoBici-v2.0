import random
from datetime import time

def topUsuariosCantidadViajes(usuarios, viajesFinalizados):
	top = {}
	for dni in viajesFinalizados:
		top[dni] = len(viajesFinalizados[dni])
	print("**** TOP 10 USUARIOS CON MAYOR CANTIDAD DE VIAJES ****")
	topOrdenado = sorted(top.items(), key = lambda x:x[1], reverse = True)
	for usuarios in topOrdenado:
		print("El usuario {} con {} viajes.".format(usuarios[0], usuarios[1]))

def topUsuariosDuracionViajes(viajesFinalizados):
	usuariosMasDuracion = {}
	for dni in viajesFinalizados:
		duracionDias = 0
		duracionHora = 0
		duracionMin = 0
		duracionSeg = 0
		for viaje in range(len(viajesFinalizados[dni])):
			salida = viajesFinalizados[dni][viaje][2]
			llegada = viajesFinalizados[dni][viaje][4]
			acumuladorSalida = (salida.hour * 3600) + (salida.minute * 60) + salida.second
			if salida <= llegada:
				acumuladorLlegada = (llegada.hour * 3600) + (llegada.minute * 60) + llegada.second
			else:
				acumuladorLlegada = ((llegada.hour + 24) * 3600) + (llegada.minute * 60) + llegada.second
			diferencia = acumuladorLlegada - acumuladorSalida
			diferenciaSegundos = diferencia % 60
			diferenciaMinutos = diferencia // 60
			if diferenciaMinutos >= 60:
				diferenciaHora = diferenciaMinutos // 60
				diferenciaMinutos = diferenciaMinutos % 60
			else:
				diferenciaHora = 0
			
			duracionHora += diferenciaHora
			duracionMin += diferenciaMinutos
			duracionSeg += diferenciaSegundos
			
		if duracionSeg >= 60:
			masMinutos = duracionSeg // 60
			segundos = diferenciaSegundos % 60
			duracionMin += masMinutos
			duracionSeg = segundos
		if duracionMin >= 60:
			masHoras = duracionMin // 60
			minutos = duracionMin % 60
			duracionHora += masHoras
			duracionMin = minutos
		if duracionHora >= 24:
			masDias = duracionHora // 24
			horas = duracionHora % 24
			duracionDias += masDias
			duracionHora = horas
		duracion = [duracionDias, time(duracionHora, duracionMin, duracionSeg)]
		usuariosMasDuracion[dni] = duracion
	print("\n**** USUARIOS CON MAYOR TIEMPO DE VIAJE ****\n")
	topOrdenado = sorted(usuariosMasDuracion.items(), key = lambda x: x[1], reverse = True)
	contador = 1
	for usuarios in topOrdenado[0:5]:
		print(contador,"El usuario {} con {} dias y {} hs de viaje.".format(usuarios[0], usuarios[1][0], usuarios[1][1]))
		#print(contador,"El usuario {} con {} hs de viaje.".format(usuarios[0], usuarios[1]))
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
		
def viajesRobados():
	print("VIAJES ROBADOS")
