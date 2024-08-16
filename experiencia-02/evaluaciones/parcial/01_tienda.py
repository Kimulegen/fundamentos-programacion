total_compra = 0
precio_arroz = 3150
precio_aceite = 1990
precio_queso = 2150
precio_leche = 1190
cant_arroz = 0
cant_aceite = 0
cant_queso= 0
cant_leche = 0

while True:
    print("*"*20, "Menú", "*"*20)
    print("Ingrese su selección:")
    print("1.- Arroz ($3150)")
    print("2.- Aceite ($1990)")
    print("3.- Queso ($2150)")
    print("4.- Leche ($1190)")
    print("5.- Terminar compra")
    seleccion = input("> ")

    if seleccion == "1":
        cant_arroz += 1
        print(f"Usted ha seleccionado arroz, actualmente lleva {cant_arroz} arroz comprados\n")
        total_compra += precio_arroz
    elif seleccion == "2":
        cant_aceite += 1
        print(f"Usted ha seleccionado aceite, actualmente lleva {cant_aceite} aceite(s) comprados\n")
        total_compra += precio_aceite
    elif seleccion == "3":
        cant_queso += 1
        print(f"Usted ha seleccionado queso, actualmente lleva {cant_queso} queso(s) comprados\n")
        total_compra += precio_queso
    elif seleccion == "4":
        cant_leche += 1
        print(f"Usted ha seleccionado leche, actualmente lleva {cant_leche} leche(s) compradas\n")
        total_compra += precio_leche
    elif seleccion == "5":
        break
    else:
        print("Su selección es inválida, favor ingresar una opción válida\n")

total_compra_iva = round(total_compra * 1.19)
 
print(f"\nSu total a pagar es de {total_compra_iva} (con IVA incluido)")