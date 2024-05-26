# EJERCICIO 1
# PuntosAcumulados
puntos = 100000
while True:
    print("1. Ver mis puntos")
    print("2. Gastar mis puntos")
    print("3. Salir")

    try:
        op = int(input("Seleccione una opción: "))

        if op == 1:
            print(f"Usted tiene {puntos} puntos")
            print()
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
            
        elif op == 3:
            print("Cierre de sesión exitoso, adiós")
            break
        else:
            print("Error, favor ingresar una opción válida")
    except ValueError as ve:
        print(ve)    
        print("Error en la selección de la opción")
        break

# EJERCICIO 2
saldo = 500000
while True:
    print("Seleccione una opción: ")
    print("1. Ver mi Saldo")
    print("2. Retirar Dinero")
    print("3. Salir")

    try:
        option = int(input("(1-3) "))

        if option < 1 or option > 3:
            print("Ingrese una opción válida")
        else:
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
            elif option == 3:
                print("Cierre de sesión exitoso, adiós")    
                break              
    except ValueError as ve:
        print("Error en la selección de una opción")
        break

# EJERCICIO 3
#CargarTarjetaBip
sw = 1
saldo = 0
while sw == 1:
    print("1. Ver mi Saldo")
    print("2. Cargar Saldo")
    print("3. Salir")
    op = int(input("Seleccione una opción"))

    try:
        if(op > 0 and op < 4):
            if op == 1:
                print(f"Tiene un saldo de {saldo}")
                continu = int(input("presione 1) para volver atrás, presione 2) para salir"))
                if continu == 2:
                    print("Cierre de sesión exitoso, salir")
                    sw == 0
            if op == 2:
                print("¿Cuánto desea cargar?")
                print("1.- $1.000")
                print("2.- $5.000")
                print("3.- $20.000")

                continu == int(input("Seleccione la opción"))
                if continu == 1:
                    saldo = saldo + 1000
                    print(f"Carga exitosa, su saldo es de:${saldo}")
                if continu == 2:
                    saldo = saldo + 5000
                    print(f"Carga exitosa, su saldo es de:${saldo}")
                if continu == 3:
                    saldo = saldo + 20000
                    print(f"Carga exitosa, su saldo es de:${saldo}")                   
            if op == 3:
                print("Muchas gracias por ocupar el servicio, adiós")
                sw = 0
        else:
            print("Selección fuera de rango")
    except:
        print("Ingreso Erróneo")