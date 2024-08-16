#! Python3
# Supermarket simulator, where you can add products, see your products and see the total cost of the purchase

import os

# initialize variables
canasta = {}
total = 0

# main menu
while True:
    print(" Menú ".center(30, "="))
    print("1. Agregar productos")
    print("2. Ver canasta")
    print("3. Ver total")
    print("4. Salir")
    choice = input("> ")
    print()

    # add products feature
    if choice == "1":
        os.system("cls||clear")
        print("Seleccione producto a agregar".center(29, "="))
        print("=" * 29)
        print("1. Arroz $2350")
        print("2. Tallarines $1190")
        print("3. Aceite $2290")
        print("4. Mermelada $1450")
        print("5. Cereal $2690")
        product = input("> ")
        print()

        os.system("cls||clear")
        if product == "1":
            canasta.setdefault("arroz", 0)
            canasta["arroz"] += 1
            total += 2350
            print(f"arroz añadido con éxito")
        elif product == "2":
            canasta.setdefault("tallarines", 0)
            canasta["tallarines"] += 1
            total += 1190
            print(f"tallarines añadido con éxito")
        elif product == "3":
            canasta.setdefault("aceite", 0)
            canasta["aceite"] += 1
            total += 2290
            print(f"aceite añadido con éxito")
        elif product == "4":
            canasta.setdefault("mermelada", 0)
            canasta["mermelada"] += 1
            total += 1450
            print(f"mermelada añadido con éxito")
        elif product == "5":
            canasta.setdefault("cereal", 0)
            canasta["cereal"] += 1
            total += 2690
            print(f"cereal añadido con éxito")
        else:
            print("Opción inválida")
        print()

    # print all products feature
    elif choice == "2":
        os.system("cls||clear")
        for k, v in canasta.items():
            print(f"{v} {k}")
        print()

    # show total feature
    elif choice == "3":
        os.system("cls||clear")
        print(f"Su total a pagar es: {total}")
        print()

    # exit menu
    elif choice == "4":
        print("Adiós")
        break

    # catch all in case user inputs invalid option
    else:
        os.system("cls||clear")
        print("Error, opción inválida\n")
