def cargarArchivos():
	usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados = dict(), dict(), dict(), dict(), dict()
	archBicicletas = open("bicicletas.csv", "r")
	archEstaciones = open("estaciones.csv", "r")
	archViajesFinalizados = open("viajes.csv", "r")
	chequearUsuariosMaestro(usuarios)
	#cargarArchivoEnMemoria(archBicicletas, bicicletas)
	#cargarArchivoEnMemoria(archEstaciones, estaciones)
	#cargarArchivoEnMemoria(archViajesFinalizados, viajesFinalizados)
	return usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados


def chequearUsuariosMaestro(usuarios):
	try:
		archUsuariosMaestro = open("usuariosMaestro.csv", "r")
		print("[INFO] No se han unificado los usuarios ya que un archivo maestro fue encontrado en el sistema.")
	except FileNotFoundError:
		archivoUsuariosMaestro = unificarUsuarios()
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
		while menor == int(listaU4[2]):
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
		usuarios[usuario[2]] = [usuario[3], usuario[0].lower().replace(" ", "_"), usuario[1]]
		usuario = leer(archUsuariosMaestro, fin)

def leer(archivo, fin):
	linea = archivo.readline()
	lista = linea.rstrip().split(",")
	return lista if linea else fin
