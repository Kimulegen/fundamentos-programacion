#! Python3
# See and use points

# initilize variables
puntos = 100000

# menu
while True:
    print("1. Ver mis puntos")
    print("2. Gastar mis puntos")
    print("3. Salir")

    try:
        op = int(input("Seleccione una opción: "))

        # Show points
        if op == 1:
            print(f"Usted tiene {puntos} puntos")
            print()

        # Use points
        elif op == 2:
            print()
            print("Seleccione el producto a canjear")
            print("1.- Gift Card de $10.000 valor de: 10.000 puntos")
            print("2.- Secadora de pelo, valor de: 25.000 puntos")
            print("3.- Disco duro portátil, valor de: 30.000 puntos")

            try:
                continu = int(input("Seleccione la opción: "))
                if continu == 1:
                    if puntos < 10000:
                        print(f"Error en canjear producto, Usted tiene {puntos} puntos")
                    else:
                        puntos = puntos - 10000
                        print(f"Canje exitoso, le quedan: ${puntos} puntos")
                if continu == 2:
                    if puntos < 25000:
                        print(f"Error en canjear producto, Usted tiene {puntos} puntos")
                    else:
                        puntos = puntos - 25000
                        print(f"Canje exitoso, le quedan: ${puntos} puntos")
                if continu == 3:
                    if puntos < 30000:
                        print(f"Error en canjear producto, Usted tiene {puntos} puntos")
                    else:
                        puntos = puntos - 30000
                        print(f"Canje exitoso, le quedan: ${puntos} puntos")
                print()
            except ValueError as ve:
                print(ve)
                print("Error en la selección de la opción")
                break

        # exit menu
        elif op == 3:
            print("Cierre de sesión exitoso, adiós")
            break

        # handle invalid inputs
        else:
            print("Error, favor ingresar una opción válida")

    # handle exceptions
    except ValueError as ve:
        print(ve)
        print("Error en la selección de la opción")
        break
