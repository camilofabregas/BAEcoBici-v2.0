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

def acumularViajes(usuario, viajesFinalizados, bicicletaAsignada, estacionRetirar, estacionDevolver, horarioSalida, horarioLlegada): #esta la saque del tp para guardar los viajes en el diccionario
	horaSalida, minSalida, segSalida = horarioSalida
	horaLlegada, minLlegada, segLlegada = horarioLlegada
	if usuario not in viajesFinalizados:
		viajesFinalizados[usuario] = [(bicicletaAsignada, estacionRetirar, time(horaSalida, minSalida, segSalida), estacionDevolver, time(horaLlegada, minLlegada, segLlegada))]
	else:
		viajesFinalizados[usuario].append((bicicletaAsignada, estacionRetirar, time(horaSalida, minSalida, segSalida), estacionDevolver, time(horaLlegada, minLlegada, segLlegada)))

def topUsuariosDuracionViajes(viajesFinalizados): #esta la saque de informes para ver si se imprimia bien este informe
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
	for usuarios in topOrdenado[0:5]:
		print(contador,"El usuario {} con {} hs de viaje.".format(usuarios[0], usuarios[1]))
		contador +=1


def leer(archivo, fin):
	linea = archivo.readline()
	lista = linea.rstrip().split(",")
	return lista if linea else fin

viajesFinalizados = {}
cargarViajesFinalizados(viajesFinalizados)
topUsuariosDuracionViajes(viajesFinalizados)
#print(viajesFinalizados)