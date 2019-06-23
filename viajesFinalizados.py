from datetime import *

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

def leer(archivo, fin):
	linea = archivo.readline()
	lista = linea.rstrip().split(",")
	return lista if linea else fin

viajesFinalizados = {}
cargarViajesFinalizados(viajesFinalizados)
topUsuariosDuracionViajes(viajesFinalizados)
#print(viajesFinalizados)