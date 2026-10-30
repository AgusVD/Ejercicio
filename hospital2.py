
elif opcion == "2"
    lista_trabajadores = []
    while len(lista_trabajadores) < 20:
        edad = input("Edad del trabajador (o salir): ")
        if edad.lower() == "salir":
            break
        while not edad.isdigit():
            edad = input("Error. Ingrese un numero: ")
        edad = int(edad)

        if edad >=15:
            lista_trabajadores.append(edad)

        else:
            print("Debe ser mayor o igual a 18.")
    print("Registrados: ", lista_trabajadores)

