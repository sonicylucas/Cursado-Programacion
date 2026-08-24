print("***** Horno Industrial ******")
while True:
    temperatura = input("Ingrese La Temperatira O Escriba FIN: ")
    if temperatura == "FIN":
        break
    elif temperatura.count(".") > 1:
        print("Error: Demasiados Puntos")
    elif  temperatura == "" or temperatura == ".":
        print("Error: Temperatura Invalida")
    elif not temperatura.replace(".", "").isdigit():
        print("Error: La Temperatura Contiene Caracteres No Validos")
    else:
        temperatura = float(temperatura)
        if temperatura < 100.0 or temperatura > 500.0:
           print("¡ADVERTENCIA! Temperatura fuera de rango")
        print(f"Temperatura Registrada: {temperatura}°C")