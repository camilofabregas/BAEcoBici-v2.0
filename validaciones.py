def solicitarValidarDigitos(mini, maxi, msj):
	dato = input(msj)
	while not dato.isdigit() or len(dato)< mini or len(dato)> maxi:
		if mini != maxi:
			print("\n[ERROR] El dato debe estar expresado en números y con una longitud de {} a {} caracteres.".format(mini, maxi))
		else:
			print("\n[ERROR] El dato debe estar expresado en números y con una longitud de {} caracteres.".format(maxi))
		dato = input(msj)
	return dato

def solicitarValidarDatos(msj):
	dato = input(msj)
	while not dato.isalpha():
		print("\n[ERROR] El dato debe estar expresado unicamente en caracteres, sin símbolos especiales y sin espacios.")
		dato = input(msj)
	return dato.lower() 

def solicitarValidarCelular():
	digitos = []
	caracteresEspeciales = ["(",")","+","-"," "," "," "," "]
	valido = True
	while len(digitos) < 8 or valido == False:
		digitos = []
		valido = True
		celular = input("[SOLICITUD] Ingrese celular pudiendo utilizar '()+-' como caracteres adicionales: ")
		for caracter in celular:
			if caracter.isdigit():
				digitos.append(caracter)
			elif caracter in caracteresEspeciales:
				caracteresEspeciales.remove(caracter)
			else:
				valido = False
	return celular
