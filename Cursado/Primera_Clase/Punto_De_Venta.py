valor_hamburguesa = 4500
valor_papasFritas = 2500
valor_bebidas = 1500
total = 0
efectivo = 0

while True:
    print("\n***** Fast Food *****")
    print("1.Agregar Hamburguesa ($4500)")
    print("2.Agregar Papas Fritas ($2000)")
    print("3.Agregar Bebida ($1500)")
    print("4.Pagar el pedido")
    print("5.Cancelar Perdido y Salir")

    option = input("Seleccione Lo Que Desea Comprar: ")

    match option:
        case "1":
            hamburguesa = input("\nIngrese La Cantidad Que Desea Llevar: ")
            while not hamburguesa.isdigit():
                hamburguesa = input("Ingrese La Cantidad Que Desea Llevar: ")
            hamburguesa = int(hamburguesa)
            total += valor_hamburguesa * hamburguesa
            print("\nHamburguesa agregada. Total actual: $", total)
        case "2":
            papasFritas = input("\nIngrese La Cantidad Que Desea Llevar: ")
            while not papasFritas.isdigit():
                papasFritas = input("\nIngrese La Cantidad Que Desea Llevar: ")
            papasFritas = int(papasFritas)
            total += valor_papasFritas * papasFritas
            print("\nPapas Fritas agregada. Total actual: $", total)
        case "3":
            bebidas = input("\nIngrese La Cantidad Que Desea Llevar: ")
            while not bebidas.isdigit():
                bebidas = input("\nIngrese La Cantidad Que Desea Llevar: ")
            bebidas = int(bebidas)
            total += valor_bebidas * bebidas
            print("\nBebidas agregadas. Total actual: $", total)
        case "4":
            efectivo = input(f'\nEl Total A Pagar Es: ${total}. Con Cuanto Efectivo Abonara?: ',)
            while not efectivo.isdigit():
                efectivo = input(f'\nEl Total A Pagar Es: ${total}. Con Cuanto Efectivo Abonara?: ',)
            efectivo = int(efectivo)
            if efectivo >= total:
                vuelto = efectivo - total
                print(f'\nEl Pago Se Ha Realizado Correctamente. Este es su vuelto: ', vuelto)
            elif efectivo < total:
                while efectivo < total:
                    print("Efectivo insuficiente. Vuelva a Ingresar: ")

        case "5":
            print("Usted Ha Cancelado El pedido")
            break
        case _:
            print("Esa opcion No Esta Disponible Vuelva A Ingresar")