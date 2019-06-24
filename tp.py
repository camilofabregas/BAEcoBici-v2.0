from imprimirMenus import *
from cargarArchivos import *
from validaciones import *
from informes import *
from datetime import *
import pickle
import random
import os

def main():
	limpiarPantalla()
	imprimirLogo() # En el módulo menuYSubmenus
	usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados, robosBicicletas = cargarArchivos()
	simularViajesPendientes(estaciones, viajesEnCurso, usuarios, bicicletas, viajesFinalizados)
	menuPrincipal(usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados, robosBicicletas)

def limpiarPantalla():
	if os.name == "nt":
		return os.system("cls")
	else:
		return os.system("clear")

def simularViajesPendientes(estaciones, viajesEnCurso, usuarios, bicicletas, viajesFinalizados):
	print("\n")
	if viajesEnCurso:
		estacionesConLugar = [] # Busco estaciones que tengan lugar (que haya por lo menos un anclaje "")
		for dni in viajesEnCurso:
			for estacion in estaciones:
				for anclaje in estaciones[estacion]["Bicicletas"]:
					if estacion not in estacionesConLugar and estaciones[estacion]["Bicicletas"][anclaje] == "":
						estacionesConLugar.append(estacion)
			idEstacion = random.choice(estacionesConLugar)
			guardarBicicleta(0, idEstacion, viajesEnCurso, usuarios, dni, estaciones, bicicletas, viajesFinalizados) # Llamo a la función guardarBicicleta con choice = 0
			# Ir a la función para saber qué es choice = 0
	arch = open("viajesEnCurso.bin", "wb") # Limpio (vacío) el archivo binario de viajesEnCurso.
	arch.close()
	viajesEnCurso.clear()

def menuPrincipal(usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados, robosBicicletas):
	opcionElegida = 0
	while opcionElegida != 5:
		imprimirMenuPrincipal() # En el módulo menuYSubmenus
		opcionElegida = ingresarEntreRangos(1,5," [SOLICITUD] Ingrese el número de opción (1 a 5): ")
		submenuElegido(opcionElegida, usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados, robosBicicletas)

def ingresarEntreRangos(inicio, fin, mensaje): #Para ingresar (y validar) una opción dentro de un rango especifico.
	opcion = input(mensaje)
	while not opcion.isdigit() or int(opcion) < inicio or int(opcion) > fin:
		print("\n[ERROR] Debe estar dentro del rango especificado.")
		opcion = input(mensaje)
	limpiarPantalla()
	return int(opcion)

def submenuElegido(opcionElegida, usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados, robosBicicletas): # Genera el submenu de la opción que elegí en el menu principal
	if opcionElegida != 4 and opcionElegida != 5: # Si no es ni "Salir del programa" ni "Ingresar al sistema"
		rangoSubmenuElegido = calcularRangoSubmenuElegido(opcionElegida)
		opcionSubmenu = 0
		while opcionSubmenu != rangoSubmenuElegido:
			imprimirSubmenuElegido(opcionElegida) # En el módulo menuYSubmenus
			opcionSubmenu = ingresarEntreRangos(1,rangoSubmenuElegido,"[SOLICITUD] Ingrese el número de opción (1 a {}): ".format(rangoSubmenuElegido))
			invocarFuncionSubmenuElegido(opcionElegida, opcionSubmenu, usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados, robosBicicletas)
	elif opcionElegida == 4:
		menuUsuario(usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados, robosBicicletas)

def calcularRangoSubmenuElegido(opcionElegida):
	if opcionElegida == 1:
		return 5
	elif opcionElegida == 2:
		return 3
	elif opcionElegida == 3:
		return 6

def invocarFuncionSubmenuElegido(opcionElegida, opcionSubmenu, usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados, robosBicicletas):
	if opcionElegida == 1 and opcionSubmenu == 1:
		listado(usuarios)
	elif opcionElegida == 1 and opcionSubmenu == 2:
		alta(usuarios)
	elif opcionElegida == 1 and opcionSubmenu == 3:
		modificacion(usuarios)
	elif opcionElegida == 1 and opcionSubmenu == 4:
		desbloquear(usuarios)
	elif opcionElegida == 2 and opcionSubmenu == 1:
		viajeAleatorio(usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados)
	elif opcionElegida == 2 and opcionSubmenu == 2:
		viajesAleatoriosMultiples(usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados)
	elif opcionElegida == 3 and opcionSubmenu == 1:
		topUsuariosCantidadViajes(usuarios, viajesFinalizados) # En el módulo informes
	elif opcionElegida == 3 and opcionSubmenu == 2:
		topUsuariosDuracionViajes(viajesFinalizados) # En el módulo informes
	elif opcionElegida == 3 and opcionSubmenu == 3:
		bicicletasEnReparacion(bicicletas) # En el módulo informes
	elif opcionElegida == 3 and opcionSubmenu == 4:
		estacionesMasActivas(estaciones, viajesFinalizados) # En el módulo informes
	elif opcionElegida == 3 and opcionSubmenu == 5:
		viajesRobados(robosBicicletas)
		
def cargarDatos(usuarios, bicicletas, estaciones, tipoDeCarga):
	generarUsuarios(usuarios) # En el módulo generarEstructuras
	generarBicicletas(bicicletas) # En el módulo generarEstructuras
	generarEstaciones(estaciones, bicicletas, tipoDeCarga) # En el módulo generarEstructuras
	limpiarPantalla()
	print("\n\n[INFO] Se ha realizado una carga automática {} de datos de usuarios, bicicletas y estaciones.\n[INFO] Volviendo al submenú de carga de datos...".format(tipoDeCarga))

def listado(usuarios):
    lista = []
    cont = 0
    for dni, datos in zip(list(usuarios.keys()), list(usuarios.values())):
        lista.append((dni, datos))
    lista.sort(key=lambda x:x[1][1])
    print("\n\n**** LISTADO DE USUARIOS ****")
    for usuario in lista:
        cont +=1
        print("{}. {}, DNI {}, PIN {}, Celular {}".format(cont, usuario[1][1], usuario[0], usuario[1][0], usuario[1][2]))

def alta(usuarios):
	dni = int(solicitarValidarDigitos(7, 8, "\n[SOLICITUD] Ingrese su DNI (sin puntos ni espacios): "))
	if dni not in usuarios:
		pin = solicitarValidarDigitos(4, 4, "[SOLICITUD] Ingrese un PIN de 4 dígitos: ")
		nombre = solicitarValidarDatos("[SOLICITUD] Ingrese su nombre: ")
		apellido = solicitarValidarDatos("[SOLICITUD] Ingrese su apellido: ")
		celular = solicitarValidarCelular()
		usuarios[dni] = [pin, nombre + "_" + apellido, celular]
		grabarEnUsuariosMaestro(usuarios)
		limpiarPantalla() 
		print("\n[EXITO] ¡Felicitaciones, {}, te has registrado con éxito!".format(nombre + "_" + apellido))
		return usuarios
	else:
		print("\n\n[ERROR] El DNI ingresado ya está asociado a una cuenta en el sistema. Volviendo al menú principal...")

def grabarEnUsuariosMaestro(usuarios):
	arch = open("usuariosMaestro.csv", "w")
	usuariosOrdenados = sorted(usuarios.items(), key = lambda x:x[0])
	for usuario in usuariosOrdenados:
		nom, ape = usuario[1][1].split("_")
		arch.write("{} {},{},{},{}\n".format(nom.title(), ape.title(), usuario[1][2], usuario[0], usuario[1][0]))
	arch.close()

def modificacion (usuarios):
	opcionElegida = 0 
	while opcionElegida != 5:
		imprimirMenuModificacion()
		opcionElegida = ingresarEntreRangos(1, 5, "[SOLICITUD] Ingrese el número de opción (1 a 5): ")
		if opcionElegida != 5:
			dni = input("\n[SOLICITUD] Ingrese el DNI: ")
			if dni.isdigit() and int(dni) in usuarios:
				dni = int(dni)
				modificarPin(opcionElegida, usuarios, dni)
				modificarNomApe(opcionElegida, usuarios, dni)
				modificarCelular(opcionElegida, usuarios, dni)
				eliminarUsuario(opcionElegida, usuarios, dni)
			else:
				limpiarPantalla()
				print ("\n[ERROR] El DNI ingresado no se encuentra en el sistema. Volviendo al menu de modificación... \n")	

def modificarPin(opcionElegida, usuarios, dni):
	if opcionElegida == 1:
		pin = input("[SOLICITUD] Ingrese el PIN asociado: ")
		while usuarios[dni][0] != pin:
			print("\n[ERROR] El PIN ingresado no es correcto")
			pin = input("[SOLICITUD] Ingrese el PIN asociado: ")
		limpiarPantalla()
		cambiarPin(usuarios, dni, pin)

def modificarNomApe(opcionElegida, usuarios, dni):
	if opcionElegida == 2:
		nombre = solicitarValidarDatos("[SOLICITUD] Ingrese su nombre: ")
		apellido = solicitarValidarDatos("[SOLICITUD] Ingrese su apellido: ")
		usuarios[dni][1] = nombre + "_" + apellido
		grabarEnUsuariosMaestro(usuarios)
		limpiarPantalla()
		print ("\n[INFO] Nombre y apellido del usuario {} fue cambiado con éxito.".format(dni))

def modificarCelular(opcionElegida, usuarios, dni):
	if opcionElegida == 3:
		celular = solicitarValidarCelular()
		usuarios [dni][2] = celular
		grabarEnUsuariosMaestro(usuarios)
		print ("[INFO] Celular del usuario {} cambiado con exito.".format(dni))

def eliminarUsuario(opcionElegida, usuarios, dni):
	if opcionElegida == 4:
		confirmacion = input("El usuario de DNI {} será eliminado. ¿Desea confirmar? s/n: ".format(dni))
		if confirmacion == "s":
			del usuarios[dni]
			grabarEnUsuariosMaestro(usuarios)
			limpiarPantalla()
			print("\n[INFO] El usuario {} fue eliminado con éxito.".format(dni))
		else:
			limpiarPantalla()
			print ("\n[INFO] Operacion cancelada. Volviendo al menu de modificación...\n")

def imprimirUsuariosBloqueados (usuarios): # Para la función desbloquear
    cantidadUsuariosBloqueados = 0 # Indice para imprimir ordenado
    print("\n**** USUARIOS BLOQUEADOS ****")
    for usuario in usuarios:
        if usuarios[usuario][0] == "": # Filtro del diccionario los usarios bloqueados
            cantidadUsuariosBloqueados += 1
            print("{}. {} con dni {}".format(cantidadUsuariosBloqueados, usuarios[usuario][1], usuario)) #imprimo indice, nombre de usuario y dni
    return cantidadUsuariosBloqueados

def generarPin(): # Para la función desbloquear
    num = random.choice('0123456789')
    num2 = random.choice('0123456789')
    num3 = random.choice('0123456789')
    num4 = random.choice('0123456789')
    nuevoPin = num + num2 + num3 + num4 
    return nuevoPin

def desbloquear (usuarios):
    cantidadUsuariosBloqueados = imprimirUsuariosBloqueados(usuarios)
    if cantidadUsuariosBloqueados > 0:
        clave = input("\n[SOLICITUD] Ingrese palabra secreta de desbloqueo: ")
        if clave == "shimano":
            usuarioElegido = int(solicitarValidarDigitos(7, 8, "[SOLICITUD] Ingrese el DNI del usuario a desbloquear: "))
            while usuarioElegido not in usuarios or usuarios[usuarioElegido][0] != "":
            	print("\n[ERROR] El DNI ingresado no corresponde a un usuario bloqueado.")
            	usuarioElegido = int(solicitarValidarDigitos(7, 8, "[SOLICITUD] Ingrese el DNI del usuario a desbloquear: "))
            usuarios[usuarioElegido][0] = generarPin()
            grabarEnUsuariosMaestro(usuarios)
            limpiarPantalla()
            print("\n[INFO] {} fue desbloqueado. Se le generó el PIN {}. Volviendo al menu de usuarios...".format(usuarios[usuarioElegido][1], usuarios[usuarioElegido][0]))
        else:
        	limpiarPantalla()
        	print("\n[ERROR] Palabra secreta incorrecta. Volviendo al menu de usuarios...")
    else:
        print("[INFO] No hay usuarios bloqueados, volviendo al menu de usuarios...")			
	
def viajeAleatorio(usuarios, bicicletas, estaciones, usuariosEnViaje, viajesFinalizados):
	usuariosDisponibles = [usuario for usuario in usuarios if usuarios[usuario][0] != "" and usuario not in usuariosEnViaje]
	if usuariosDisponibles:
		usuario = random.choice(usuariosDisponibles)
		estacionRetirar, bicicletaAsignada = retiroAleatorioBicicleta(estaciones, bicicletas)
		horarioSalida = horarios(0, 0, 0, 23, 30, 60)
		print("\n{} retiró la bicicleta {} de la estación N°{} de {} a las {}:{}:{}hs".format(usuarios[usuario][1], bicicletaAsignada, estacionRetirar, estaciones[estacionRetirar]["Dirección"], horarioSalida[0], horarioSalida[1], horarioSalida[2]))
		estacionDevolver = devolucionAleatoriaBicicleta(estaciones, bicicletaAsignada, estacionRetirar)
		duracionViaje = horarios(0, 0, 0, 2, 30, 60)  # maximo 90 minutos que equivale a 1:30:00hs
		horarioLlegada = calcularHoraLlegada(horarioSalida, duracionViaje)
		print("{} devolvió la bicicleta {} en la estación N°{} de {} a las {}:{}:{}hs".format(usuarios[usuario][1], bicicletaAsignada, estacionDevolver, estaciones[estacionDevolver]["Dirección"], horarioLlegada[0], horarioLlegada[1], horarioLlegada[2]))
		bloqueoExcesoHorario(1, usuarios, duracionViaje, usuario)
		acumularViajes(usuario, viajesFinalizados, bicicletaAsignada, estacionRetirar, estacionDevolver, horarioSalida, horarioLlegada)

def retiroAleatorioBicicleta(estaciones, bicicletas):
    bicicletaAsignada = ""
    while not bicicletaAsignada:
        estacionRetirar = random.randrange(1, 11)
        for anclaje in estaciones[estacionRetirar]["Bicicletas"]:
            bici = estaciones[estacionRetirar]["Bicicletas"][anclaje]
            if bici and bicicletas[bici][0] != "Necesita reparación":
                estaciones[estacionRetirar]["Bicicletas"][anclaje] = ""
                return estacionRetirar, bici

def devolucionAleatoriaBicicleta(estaciones, bici, estacionRetirar):
    estacionDevolver = estacionRetirar
    while estacionDevolver == estacionRetirar:
        estacion = random.randrange(1, 11)
        for anclaje in estaciones[estacion]["Bicicletas"]:
            if estaciones[estacion]["Bicicletas"][anclaje] == "":
                estaciones[estacion]["Bicicletas"][anclaje] = bici
                return estacion

def bloqueoExcesoHorario(chequeo, usuarios, duracionViaje, usuario):
	# Para saber qué es "chequeo", leer la explicación en la función guardarBicicleta
    if duracionViaje[0] == 1 and duracionViaje[1] >= 0:
        usuarios[usuario][0] = ""
        grabarEnUsuariosMaestro(usuarios)
        if chequeo == 1:
        	print("[AVISO] Tu cuenta fue bloqueada por exceder los 60 minutos de viaje.")
        	return 0
        else:
        	return 1


def acumularViajes(usuario, viajesFinalizados, bicicletaAsignada, estacionRetirar, estacionDevolver, horarioSalida, horarioLlegada):
	horaSalida, minSalida, segSalida = horarioSalida
	horaLlegada, minLlegada, segLlegada = horarioLlegada
	if usuario not in viajesFinalizados:
		viajesFinalizados[usuario] = [(bicicletaAsignada, estacionRetirar, time(horaSalida, minSalida, segSalida), estacionDevolver, time(horaLlegada, minLlegada, segLlegada))]
	else:
		viajesFinalizados[usuario].append((bicicletaAsignada, estacionRetirar, time(horaSalida, minSalida, segSalida), estacionDevolver, time(horaLlegada, minLlegada, segLlegada)))

def viajesAleatoriosMultiples(usuarios, bicicletas, estaciones, usuariosEnViaje, viajesFinalizados):
	cantidad = ingresarEntreRangos(1, 100, "\n[SOLICITUD] Ingrese entre 1 y 100 la cantidad de viajes aleatorios que desea generar: ")
	for viaje in range(cantidad):
		viajeAleatorio(usuarios, bicicletas, estaciones, usuariosEnViaje, viajesFinalizados)
		usuariosDisponibles = [usuario for usuario in usuarios if usuarios[usuario][0] != "" and usuario not in usuariosEnViaje]
		if not usuariosDisponibles:
			print("\n\n[INFO] No hay usuarios disponibles. Se encuentran todos bloqueados o actualmente en viaje")
			return None

def calcularHoraLlegada(horarioSalida, duracionViaje):
	horaLlegada = horarioSalida[0] + duracionViaje[0]
	minLlegada = horarioSalida[1] + duracionViaje[1]
	segLlegada = horarioSalida[2] + duracionViaje[2]
	if segLlegada >= 60:
		segLlegada = segLlegada - 60
		minLlegada += 1
	if minLlegada >= 60:
		minLlegada = minLlegada - 60
		horaLlegada +=1
	return (horaLlegada, minLlegada, segLlegada)

def menuUsuario(usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados, robosBicicletas):
	dni, pin = iniciarSesion(usuarios)
	if dni != 0:
		opcionElegida = 0
		while opcionElegida != 5:
			imprimirMenuUsuario()
			opcionElegida = ingresarEntreRangos(1,5,"[SOLICITUD] Ingrese el número de opción (1 a 5): ")
			submenuUsuario(usuarios, bicicletas, estaciones, opcionElegida, dni, pin, viajesEnCurso, viajesFinalizados, robosBicicletas)

def iniciarSesion(usuarios):
	print("\n\n**** INICIAR SESIÓN ****")
	dni = input("[SOLICITUD] Ingrese su DNI: ")
	if dni.isdigit() and int(dni) in usuarios:
		if usuarios[int(dni)][0] == "":
			limpiarPantalla()
			print("\n[ERROR] Su cuenta se encuentra bloqueada, volviendo al menu principal...")
			return 0, 0
		pin = input("[SOLICITUD] Ingrese su PIN asociado: ")
		while pin != usuarios[int(dni)][0]:
			pin = input("\n[ERROR] PIN incorrecto, pruebe de nuevo.\n[SOLICITUD] Ingrese su PIN asociado: ")
		limpiarPantalla()
		print("\n[MENSAJE] Iniciaste sesión con éxito. ¡Bienvenido, {}!".format(usuarios[int(dni)][1]))
		return int(dni), pin
	else:
		limpiarPantalla()
		print("\n[ERROR] No hay una cuenta registrada con ese DNI, volviendo al menu principal...")
		return 0, 0

def submenuUsuario(usuarios, bicicletas, estaciones, opcionElegida, dni, pin, viajesEnCurso, viajesFinalizados, robosBicicletas):
	if opcionElegida == 1:
		cambiarPin(usuarios, dni, pin)
	elif opcionElegida == 2:
		retirarBicicleta(usuarios, bicicletas, estaciones, dni, viajesEnCurso, robosBicicletas)
	elif opcionElegida == 3:
		devolverBicicleta(estaciones, dni, viajesEnCurso, usuarios, bicicletas, viajesFinalizados)
	elif opcionElegida == 4:
		robarBicicleta(viajesEnCurso, usuarios, bicicletas, dni, robosBicicletas)

def cambiarPin(usuarios, dni, pinViejo):
	if usuarios[dni][0] != "":
		print("\n")
		pinNuevo = solicitarValidarDigitos(4, 4,"[SOLICITUD] Ingrese un nuevo PIN de 4 dígitos: ")
		while pinNuevo == pinViejo:
			print("\n[ERROR] El PIN ingresado ya está asociado a su cuenta.")
			pinNuevo = solicitarValidarDigitos(4, 4,"[SOLICITUD] Ingrese un nuevo PIN de 4 dígitos: ")
		pinNuevoRepetido = solicitarValidarDigitos(4, 4,"[SOLICITUD] Ingrese nuevamente el PIN deseado: ")
		while pinNuevo != pinNuevoRepetido:
			print("\n[ERROR] Los pines no coinciden, intente de nuevo...")
			pinNuevoRepetido = solicitarValidarDigitos(4, 4,"[SOLICITUD] Ingrese nuevamente el PIN deseado: ")
		usuarios[dni][0] = pinNuevo
		grabarEnUsuariosMaestro(usuarios)
		limpiarPantalla()
		print("\n[INFO] El PIN fue cambiado con éxito. Volviendo al menu de usuario...")
	else:
		limpiarPantalla()
		print("\n[ERROR] Su usuario se encuentra bloqueado. Volviendo al menu de usuario...")

def retirarBicicleta (usuarios, bicicletas, estaciones, dni, viajesEnCurso, robosBicicletas): # Verifica que el usuario no esté en viaje ni bloqueado y pide el PIN.
	if dni in viajesEnCurso or usuarios[dni][0] == "":
		print("\n[ERROR] El usuario {} está bloqueado o actualmente se encuentra en viaje.".format(usuarios[dni][0]))
	else:
		contador = 4
		pin = input("\n[SOLICITUD] Ingrese su numero de PIN: ")
		while contador > 1 and pin != usuarios[dni][0]:
			contador += -1
			pin = input("[ERROR] Por favor, ingrese su numero de pin correctamente. Tiene {} intentos restantes: ".format(contador))
			if contador == 1:
				usuarios[dni][0] = ""
				grabarEnUsuariosMaestro(usuarios)
				limpiarPantalla()
				print ("\n[INFO] El usuario {} fue bloqueado porque excedió la cantidad de intentos permitidos.".format(usuarios[dni][1]))
				return None
		elegirEstacionParaRetirar(estaciones, bicicletas, viajesEnCurso, dni, robosBicicletas)

def elegirEstacionParaRetirar(estaciones, bicicletas, viajesEnCurso, dni, robosBicicletas):
	print("\n**** ESTACIONES ****")
	for estacion in estaciones:
		print("Estación {}: {}".format(estacion, estaciones[estacion]["Dirección"]))
	idEstacion = int(solicitarValidarDigitos(1, len(estaciones), "\n[SOLICITUD] Ingrese el numero de identificacion de la estacion donde desea retirar la bicicleta: "))
	while idEstacion not in estaciones or len(estaciones[idEstacion]["Bicicletas"]) == 0:
		print("\n[ERROR] El número de estación ingresado es inválido o la estación se encuentra sin bicicletas.")
		idEstacion = int(solicitarValidarDigitos(1, len(estaciones), "[SOLICITUD] Ingrese el numero de identificacion de la estacion donde desea retirar la bicicleta: "))
	asignarBicicleta(estaciones, bicicletas, viajesEnCurso, idEstacion, dni, robosBicicletas)

def asignarBicicleta(estaciones, bicicletas, viajesEnCurso, idEstacion, dni, robosBicicletas):
	anclajeParaRetirar = random.randrange(1,len(estaciones[idEstacion]["Bicicletas"]))
	while estaciones[idEstacion]["Bicicletas"][anclajeParaRetirar] == "":
		anclajeParaRetirar = random.randrange(1,len(estaciones[idEstacion]["Bicicletas"]))
	bicicletaRetirada = estaciones[idEstacion]["Bicicletas"][anclajeParaRetirar]
	limpiarPantalla()
	print("\n[EXITO] Acerquese al anclaje {} y retire la bicicleta {}.\n".format(anclajeParaRetirar,bicicletaRetirada))
	estaciones[idEstacion]["Bicicletas"][anclajeParaRetirar] = ""
	horas, minutos, segundos = horarios (0, 0, 0, 23, 60, 60)
	while (horas == 22) and (minutos > 44):
		horas, minutos, segundos = horarios (0, 0, 0, 23, 60, 60)
	horarioSalida = time(horas, minutos, segundos)
	bicicletas[bicicletaRetirada] = ["En condiciones", "En circulacion"]
	viajesEnCurso[dni] = [bicicletaRetirada, idEstacion, horarioSalida]
	grabarRobosYViajesEnCurso("viajesEnCurso.bin", robosBicicletas, dni, '', bicicletaRetirada, idEstacion, horarioSalida)

def devolverBicicleta(estaciones, dni, viajesEnCurso, usuarios, bicicletas, viajesFinalizados):
    if dni not in viajesEnCurso:
        print("\n[INFO] Usted no ha retirado una bicicleta. Volviendo al submenu...")
    else:
        print("\n**** ESTACIONES ****")
        for estacion in estaciones:
            print("Estación {}: {}".format(estacion, estaciones[estacion]["Dirección"]))
        idEstacion = int(solicitarValidarDigitos(1, 10, "[SOLICITUD] Ingrese el número de la estación donde devolverá la bicicleta: "))
        while idEstacion not in estaciones:
            idEstacion = int(solicitarValidarDigitos(1, 10, "[ERROR]Ingrese un número de estación válido: "))
        verificarLugar(idEstacion, estaciones, viajesEnCurso, usuarios, dni, bicicletas, viajesFinalizados)

def verificarLugar(idEstacion, estaciones, viajesEnCurso, usuarios, dni, bicicletas, viajesFinalizados): #Se fija si hay lugar en la estación elegida para anclar la bici.
	anclajesLibres = 0
	for anclaje in estaciones[idEstacion]["Bicicletas"]:
		if estaciones[idEstacion]["Bicicletas"][anclaje] == "":
			anclajesLibres += 1
	if len(estaciones[idEstacion]["Bicicletas"]) - anclajesLibres >= estaciones[idEstacion]["Capacidad"]:
		print("[INFO] No hay lugar en esta estación para anclar su bicicleta. Por favor diríjase hacia otra estación.")
	else:
		guardarBicicleta(1, idEstacion, viajesEnCurso, usuarios, dni, estaciones, bicicletas, viajesFinalizados)

def guardarBicicleta(chequeo, idEstacion, viajesEnCurso, usuarios, dni, estaciones, bicicletas, viajesFinalizados): #Ancla bicicleta a estación elegida o la envía a reparar.
	# Chequeo = 0 signfica que entramos acá para simular viajes.
	# Chequeo = 1 significa que entramos acá porque un usuario real quiere devolver una bicicleta.
	idBicicleta = viajesEnCurso[dni][0]
	if chequeo == 0:
		estadoBici = "n" # Como el chequeo es 0, salteo la pregunta de reparar bici.
	else:
		estadoBici = input("\n[SOLICITUD] ¿Necesita reparación la bicicleta? s/n: ")
	while estadoBici != "s" and estadoBici != "n":
		print("[ERROR] Ingrese una opción válida.")
		estadoBici = input("\n[SOLICITUD] ¿Necesita reparación la bicicleta? s/n: ")
	if estadoBici == "s":
		bicicletas[idBicicleta][0] = "Necesita reparación"
		bicicletas[idBicicleta][1] = "En reparación"
		print("[INFO] La bicicleta se enviará a reparación.")
	else:
		for anclaje in estaciones[idEstacion]["Bicicletas"]:
			if estaciones[idEstacion]["Bicicletas"][anclaje] == "":
				estaciones[idEstacion]["Bicicletas"][anclaje] = idBicicleta
				bicicletas[idBicicleta][1] = "Anclada en estación"
	duracionViaje = horarios(0, 0, 0, 2, 15, 60)
	horarioSalida = (abs(viajesEnCurso[dni][2].hour), abs(viajesEnCurso[dni][2].minute), abs(viajesEnCurso[dni][2].second))
	horarioLlegada = calcularHoraLlegada(horarioSalida, duracionViaje)
	fueBloqueado = bloqueoExcesoHorario(chequeo, usuarios, duracionViaje, dni)
	acumularViajes(dni, viajesFinalizados, idBicicleta, viajesEnCurso[dni][1], idEstacion, horarioSalida, horarioLlegada)
	if chequeo == 1:
		del(viajesEnCurso[dni])
		arch = open("viajesEnCurso.bin", "wb") # Limpio (vacío) el archivo binario de viajesEnCurso.
		arch.close()
	else:
		if fueBloqueado == 1:
			print("[SIMULACIÓN] El usuario {} devolvió la bicicleta en la estación {} a las {} horas. \n             Además, fue bloqueado por superar la hora de viaje.\n".format(usuarios[dni][1], estaciones[idEstacion]["Dirección"], str(horarioLlegada[0])+":"+str(horarioLlegada[1])+":"+str(horarioLlegada[2])))
		else:
			print("[SIMULACIÓN] El usuario {} devolvió la bicicleta en la estación {} a las {} horas.\n".format(usuarios[dni][1], estaciones[idEstacion]["Dirección"], str(horarioLlegada[0])+":"+str(horarioLlegada[1])+":"+str(horarioLlegada[2])))
	
def horarios (horaMinimo, minutosMinimo, segundosMinimo, horaMaximo, minutosMaximo, segundosMaximo):
	horas = random.randrange(horaMinimo, horaMaximo)
	minutos = random.randrange(minutosMinimo, minutosMaximo)
	segundos = random.randrange(segundosMinimo, segundosMaximo)
	return (horas, minutos, segundos)

def robarBicicleta(viajesEnCurso, usuarios, bicicletas, dni, robosBicicletas):
	print('**** ROBAR BICICLETA ****\n')
	if dni in viajesEnCurso:
		limpiarPantalla()
		print('\n[ERROR] No puede robar una bicicleta mientras esté usando una. Volviendo al menú anterior...\n')
	else:
		idBicicletaParaRobar = int(solicitarValidarDigitos(4, 4, '\n[SOLICITUD] Ingrese el número de bicicleta que desea robar: '))
		while idBicicletaParaRobar not in bicicletas:
			idBicicletaParaRobar = int(solicitarValidarDigitos(4, 4, '\n[ERROR] La bicicleta que intenta robar no existe. Ingrese una válida: '))
		verificarBicicletaEnViaje(viajesEnCurso, idBicicletaParaRobar, usuarios, dni, robosBicicletas, bicicletas)

def verificarBicicletaEnViaje(viajesEnCurso, idBicicletaParaRobar, usuarios, dni, robosBicicletas, bicicletas):
	bicicletaYaRobada = verificarBicicletaYaRobada(robosBicicletas, viajesEnCurso, idBicicletaParaRobar, bicicletas)
	if bicicletaYaRobada:
		limpiarPantalla()
		print('[INFO] La bicicleta que intenta robar ya fue robada durante el viaje. Volviendo al menú anterior...')
	else:
		if bicicletas[idBicicletaParaRobar][1] == "En circulacion":		
			asignarBicicletaAlLadron(viajesEnCurso, robosBicicletas, usuarios, dni, idBicicletaParaRobar)
		else:
			usuarios[dni][0] = ""
			limpiarPantalla()
			print("[INFO] La bicicleta que intentó robar está anclada a una estación. Su usuario ha sido bloqueado.\n")			

def verificarBicicletaYaRobada(robosBicicletas, viajesEnCurso, idBicicletaParaRobar, bicicletas): #Se fija si la bicicleta que se quiere robar, ya fue robada durante el mismo viaje.
	if bicicletas[idBicicletaParaRobar][1] == "En circulacion": #Se fija si la bici esta en viaje.
		for dniLadron in robosBicicletas:
			if idBicicletaParaRobar in robosBicicletas[dniLadron][1]: #Se fija si fue robada
				for dniEnCurso in viajesEnCurso:
					if dniEnCurso ==  dniLadron: #Se fija si el ladron sigue usando la bici que robo
						return True
	else:
		return False

def asignarBicicletaAlLadron(viajesEnCurso, robosBicicletas, usuarios, dni, idBicicletaParaRobar):
	for dniEnCurso in viajesEnCurso.copy():
		if viajesEnCurso[dniEnCurso][0] == idBicicletaParaRobar:
			guardarRobo(robosBicicletas, dni, idBicicletaParaRobar, usuarios, dniEnCurso, viajesEnCurso)
			borrarViajeRobado(dniEnCurso, dni, viajesEnCurso)
			viajesEnCurso[dni] = viajesEnCurso.pop(dniEnCurso) #Cambio el dni anterior por el del ladrón. Pero el resto de los datos quedan iguales.
			grabarRobosYViajesEnCurso("viajesEnCurso.bin", robosBicicletas, dni, idBicicletaParaRobar, viajesEnCurso[dni][0], viajesEnCurso[dni][1], viajesEnCurso[dni][2])
			print(viajesEnCurso)	

def guardarRobo(robosBicicletas, dni, idBicicletaParaRobar, usuarios, dniEnCurso, viajesEnCurso):
	if dni not in robosBicicletas:
		robosBicicletas[dni] = [usuarios[dni][1], []] #Al dic le agrego dni, nombre del ladrón y una lista con las bicis que robó.
		robosBicicletas[dni][1].append(idBicicletaParaRobar)
		grabarRobosYViajesEnCurso("robosBicicletas.bin", robosBicicletas, dni, idBicicletaParaRobar, '', '', '')
		print('[INFO] {} le robó la bicicleta {} a {}.\n'.format(usuarios[dni][1], idBicicletaParaRobar, usuarios[dniEnCurso][1]))
	else:
		robosBicicletas[dni][1].append(idBicicletaParaRobar)
		grabarRobosYViajesEnCurso("robosBicicletas.bin", robosBicicletas, dni, idBicicletaParaRobar, '', '', '')
		print('[INFO] {} le robó la bicicleta {} a {}.\n'.format(usuarios[dni][1], idBicicletaParaRobar, usuarios[dniEnCurso][1]))		
	return robosBicicletas

def grabarRobosYViajesEnCurso(ruta, robosBicicletas, dni, idBicicletaParaRobar, bicicletaRetirada, idEstacion, horarioSalida):
	with open(ruta, "ab") as arch:
		pkl = pickle.Pickler(arch)
		dic = []
		if ruta == "robosBicicletas.bin":			
			dic = [dni, robosBicicletas[dni][0], robosBicicletas[dni][1]]
			pkl.dump(dic)
		else:
			dic = [dni, bicicletaRetirada, idEstacion, horarioSalida]
			pkl.dump(dic)

def borrarViajeRobado(dniEnCurso, dni, viajesEnCurso): #Borra el viaje que estaba en curso del usuario antes de que le roben la bici.
	with open("viajesEnCurso.bin", "rb") as arch:
		dicAux = {}
		seguir = True
		while seguir == True:
			try:
				dato = pickle.load(arch)
				dicAux[dato[0]] = [dato[1], dato[2], dato[3]]
			except EOFError:
				seguir = False
	del(dicAux[dniEnCurso])
	arch = open("viajesEnCurso.bin", "wb") # Limpio (vacío) el archivo binario de viajesEnCurso.
	arch.close()
	for dni in dicAux:
		grabarEnViajesEnCurso(dni, dicAux[dni][0], dicAux[dni][1], dicAux[dni][2]) #Lo vuelvo a cargar sin el viaje en curso anterior.

def grabarEnViajesFinalizados(usuario, bicicletaAsignada, estacionRetirar, estacionDevolver, horarioSalida, horarioLlegada):
	viajes = open("viajes.csv", "a")
	sal = []
	lleg = []
	for numero in range(len(horarioSalida)):
		if horarioSalida[numero] < 10:
			sal.append("0"+str(horarioSalida[numero]))
		else:
			sal.append(horarioSalida[numero])
	for numero in range(len(horarioLlegada)):
		if horarioLlegada[numero] < 10:
			lleg.append("0"+str(horarioLlegada[numero]))
		else:
			lleg.append(horarioLlegada[numero])

	salida = "{}:{}:{}".format(sal[0],sal[1],sal[2])
	llegada = "{}:{}:{}".format(lleg[0],lleg[1],lleg[2])
	
	acumuladorSalida = (horarioSalida[0] * 3600) + (horarioSalida[1] * 60) + horarioSalida[2]
	if time(horarioSalida[0],horarioSalida[1],horarioSalida[2]) <= time(horarioLlegada[0],horarioLlegada[1],horarioLlegada[2]):
		acumuladorLlegada = (horarioLlegada[0] * 3600) + (horarioLlegada[1] * 60) + horarioLlegada[2]
	else:
		acumuladorLlegada = ((horarioLlegada[0] + 24) * 3600) + (horarioLlegada[1] * 60) + horarioLlegada[2]
	diferencia = acumuladorLlegada - acumuladorSalida
	diferenciaSegundos = diferencia % 60
	if diferenciaSegundos < 10:
		diferenciaSegundos = "0" + str(diferenciaSegundos)
	diferenciaMinutos = diferencia // 60
	if diferenciaMinutos >= 60:
		diferenciaHora = "0" + str(diferenciaMinutos // 60)
		diferenciaMinutos = diferenciaMinutos % 60
		if diferenciaMinutos < 10:
			diferenciaMinutos = "0" + str(diferenciaMinutos)
	else:
		diferenciaHora = "00"
	duracionViaje = "{}:{}:{}".format(diferenciaHora, diferenciaMinutos, diferenciaSegundos)

	viajes.write("{},{},{},{},{},{},{}\n".format(estacionRetirar,estacionDevolver,usuario,salida,duracionViaje,llegada,bicicletaAsignada))
	viajes.close()
main()
