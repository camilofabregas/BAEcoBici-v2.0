def imprimirMenuPrincipal():
	print(" **************************************")
	print(" *********** MENU PRINCIPAL ***********")
	print(" **************************************")
	print(" ***                                ***")
	print(" ***  1. Usuarios                   ***")
	print(" ***                                ***")
	print(" ***  2. Retiros automáticos        ***")
	print(" ***                                ***")
	print(" ***  3. Informes                   ***")
	print(" ***                                ***")
	print(" ***  4. Ingresar al sistema        ***")
	print(" ***                                ***")
	print(" ***  5. Salir del programa         ***")
	print(" ***                                ***")
	print(" **************************************")
	print(" **************************************\n")

def imprimirLogo():
	print("""\n\n     %%%%%%%%%%%%        %%%%%          &%%%%%%%%%%%                           &%%%           %%%%%             %%%%%  
    %%%%%%%%%%%%%%%     %%%%%%%         &%%%%%%%%%%%                           &%%%            %%%               %%%   
    %%%%%%%%%%%%%%%%   %%%%%%%%%        &%%%            %%%%%&      %%%%%%@    &%%% @%%%%%     %%%     @%%%%%@   &%%   
    %%%%%%%%%%%%%%%   %%%%%%%%%%%       &%%%         &%%%%%%%%%%  %%%%%%%%%%%  &%%%%%%%%%%%%  &%%%   %%%%%%%%%%  %%%%  
    %%%%%%%%%%%%%%%  %%%%%%%%%%%%%      &%%%%%%%%%% &%%%        @%%%%     %%%% &%%%%     %%%% &%%%  %%%%         %%%%  
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     &%%%        %%%         %%%%       %%% &%%%      &%%% &%%%  %%%          %%%%  
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    &%%%         %%%      @  %%%%     %%%% &%%%%     %%%% &%%%  %%%%     @   %%%%  
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%   &%%%%%%%%%%%  %%%%%%%%%%  %%%%%%%%%%%  &%%%%%%%%%%%%  &%%%   %%%%%%%%%%  %%%%  
      %%%%%%%%%%   %%%           %%%     %%%%%%%%%%     %%%%%        %%%%%      %%   %%%%%      %       %%%%%     %% """)

def imprimirSubmenuElegido(opcionElegida):
	if opcionElegida == 1:
		print("\n\n **************************************")
		print(" ************** USUARIOS **************")
		print(" **************************************")
		print(" ***                                ***")
		print(" ***  1. Listado                    ***")
		print(" ***                                ***")
		print(" ***  2. Alta                       ***")
		print(" ***                                ***")
		print(" ***  3. Modifica                   ***")
		print(" ***                                ***")
		print(" ***  4. Desbloquear                ***")
		print(" ***                                ***")
		print(" ***  5. Volver al menu principal   ***")
		print(" ***                                ***")
		print(" **************************************")
		print(" **************************************\n")
	elif opcionElegida == 2:
		print("\n\n**** RETIROS AUTOMÁTICOS ****\n    1. Viaje aleatorio\n    2. Viajes aleatorios múltiples\n    3. Volver al menu principal")
	elif opcionElegida == 3:
		print("\n\n**** INFORMES ****\n    1. Usuarios con mayor cantidad de viajes\n    2. Usuarios con mayor duración acumulada de viajes\n    3. Bicicletas en reparación\n    4. Estaciones más activas\n    5. Viajes en los que hubo robos\n    6. Volver al menu principal")

def imprimirMenuModificacion():
	print ("\n\n**** MODIFICACION DE DATOS ****")
	print("1. Modificacion de PIN")
	print("2. Modifiacion de nombre y apellido")
	print("3. Modificacion de celular")
	print("4. Eliminar usuario")
	print("5. Volver al menu anterior")

def imprimirMenuUsuario():
	print("\n\n**** MENU DEL USUARIO *****")
	print("1. Modificar PIN")
	print("2. Retirar bicicleta")
	print("3. Devolver bicicleta")
	print("4. Robar bicicleta")
	print("5. Volver al menu principal")
