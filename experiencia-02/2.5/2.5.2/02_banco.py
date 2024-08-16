#! Python3
# bank simulator

# initialize variables
saldo = 500000

# menu
while True:
    print("Seleccione una opción: ")
    print("1. Ver mi Saldo")
    print("2. Retirar Dinero")
    print("3. Salir")

    try:
        option = int(input("(1-3) "))

        # handle invalid inputs
        if option < 1 or option > 3:
            print("Ingrese una opción válida")
        else:
            # Show balance
            if option == 1:
                print(f"Tiene un saldo de ${saldo}")
                try:
                    option2 = int(input("Presione 1 para volver atrás o 2 para salir "))
                    if option2 == 1:
                        continue
                    elif option2 == 2:
                        print("Cierre de sesión exitoso, adiós")
                        break
                except ValueError as ve:
                    print("Error en la selección de una opción")
                    break

            # transfer simulator
            elif option == 2:
                transfer = int(input("Ingrese la cantidad que desea transferir: "))
                if transfer > saldo:
                    print("No se pudo realizar la transferencia")
                else:
                    saldo -= transfer
                    print(f"Transferencia realizada")
                try:
                    option2 = int(input("Presione 1 para volver atrás o 2 para salir "))
                    if option2 == 1:
                        continue
                    elif option2 == 2:
                        print("Cierre de sesión exitoso, adiós")
                        break
                except ValueError as ve:
                    print("Error en la selección de una opción")
                    break

            # exit menu
            elif option == 3:
                print("Cierre de sesión exitoso, adiós")
                break

    # handle exceptions
    except ValueError as ve:
        print("Error en la selección de una opción")
        break
