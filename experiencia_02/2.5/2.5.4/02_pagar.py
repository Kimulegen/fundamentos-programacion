while True:
    try:
        print("*"*15, end="")
        print("Menu", end="")
        print("*"*15)
        print("1.- Pagar con tarjeta de crédito")
        print("2.- Pagar con con PayPal")
        print("3.- Pagar por transferencia")
        print("4.- Cancelar")
        print("5.- Salir ")
        option = int(input("\nIngrese la opción deseada: "))

        # OPCION TARJETA
        if option == 1:
            n_tarjeta = int(input("Ingrese número de tarjeta de crédito: "))
            nombre = input("Ingrese nombre titular: ")
            mes_vencimiento = int(input("Ingrese mes de vencimiento: "))
            ano_vencimiento = int(input("Ingrese año vencimiento: "))
            print()
            print("Detalle compra")
            print(f"Costo de la compra: $100.000")
            print(f"Número de tarjeta: {n_tarjeta}")
            print(f"Nombre del titular: {nombre}")
            print(f"Mes y año: {mes_vencimiento:02}/{ano_vencimiento}")
            print()
            print("Muchas gracias por su compra")
            break
        # OPCION PAYPAL
        elif option == 2:
            user = input("Ingrese su usario: ")
            pwd = input("Ingrese su contraseña: ")
            censored_pwd = "*"*len(pwd)
            print()
            print("Detalle compra")
            print(f"Costo de la compra: $100.000")
            print(f"Usuario: {user}")   
            print(f"Contraseña: {censored_pwd}")
            print()
            print("Muchas gracias por su compra")
            break
        # OPCION TRANSFERENCIA
        elif option == 3:
            print("Datos para realizar la transferencia")
            print("Banco: Banco El País")
            print("Rut: 11.111.111-1")
            print("Número de cuenta: 123456879")
            print("Tipo de cuenta: Corriente")
            print("Código de referencia: 987654321")
            print()
            print("Muchas gracias por su compra")
            break
        # OPCION CANCELAR
        elif option == 4:
            print("Pago cancelado")
        # OPCION SALIR
        elif option == 5:
            print("Hasta pronto...")
            break
        else:
            print("Opción no válida")
    except ValueError as ve:
        print("Error, dato númerico inválido")
        break