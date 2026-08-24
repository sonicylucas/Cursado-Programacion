saldo = 50000

while True:
    print("\n***** Cajero Automatico ****")
    print("1.Consultar Saldo")
    print("2.Ingresar Dinero")
    print("3.Retirar Dinero")
    print("4.Salir")

    option = input("\nSeleccione La Consulta: ")

    match option:
        case "1":
            print("\nTu Saldo Dipsonible Es: ", saldo)
        case "2":
            dinero = input("\nIngrese El Monto A Depositar: ")
            while not dinero.isdigit():
                dinero = input("Ingrese El Monto A Depositar: ")
            dinero = int(dinero)
            saldo += dinero
            print("\nTu Nuevo Saldo Es: ", saldo)
        case "3":
            retirar = input("Ingrese La Cantidad A Retirar: ")
            while not retirar.isdigit():
                retirar = input("Ingrese La Cantidad A Retirar: ")
            retirar = int(retirar)
            saldo -= retirar
            print("\nTu Nuevo Saldo Es: ", saldo)
        case "4":
            print("\nHa Salido Del Sistema")
            break

        case _:
            print("\nOpcion Incorrecta")