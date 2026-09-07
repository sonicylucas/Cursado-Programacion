listas_especialidades = []
cupos = []




while True:
    print("\n*** Clinica ***")
    print("1.Ingresar Una Especialidad")
    print("2.Ingresar lista de cupos disponibles por especialidad ")
    print("3.Mostrar agenda ")
    print("4.Consultar cupos de una especialidad")
    print("5.Listar especialidades sin cupo ")
    print("6.Agregar especialidad")
    print("7.Actualizar cupos (reservar / cancelar) ")
    print("8.Salir")
    option = (input("Ingrese Una Opcion: "))
    
    match option:
        case "1":
            listas_especialidades = []
            cantidad_especialidades = input("Cuantas especialidades desea ingresar?: ")
            while not cantidad_especialidades.isdigit() or int(cantidad_especialidades) <= 0:
                cantidad_especialidades = input("Ingrese un numero mayor a 0: ") 
            for i in range(int(cantidad_especialidades)):
                especialidades = input(f'Ingrese la especialiad {i + 1}: ')
                listas_especialidades.append(especialidades)
            print("Listas de especialidades cargadas correctamente")
        case "2":
            if listas_especialidades == []:
                print("No hay especialidades")
            else:
                for especialidades in listas_especialidades:
                     cantidad_cupos = input(f'Ingrese los cupos para {especialidades} : ')
                     cupos.append(int(cantidad_cupos))
                print("Cupos Agregado Correctamente ")
        case "3":
                if listas_especialidades == []:
                    print("No hay especialidades")
                else:
                    print("\n *** Agenda *** ")
                    for i in range(len(listas_especialidades)):
                        if i < len(cupos):
                            cantidad_cupos = cupos[i]
                        else:
                            cantidad_cupos = "Sin asignar"
                        print(f'{listas_especialidades[i]}: {cantidad_cupos} cupos')
        case "4":
            print("queso")
        case "5":
            print("queso")
        case "6":
            nueva_especialidad = input("Ingrese Una Nueva Especialidad: ")
            listas_especialidades.append(nueva_especialidad)
            print("\nEspecialidad Agregada ")
        case "7":
            print("queso")
        case "8":
            print("Salio De La Clinica")
            break
        case _:
            print("No Es Una Opcion Vuelva a Intentar")