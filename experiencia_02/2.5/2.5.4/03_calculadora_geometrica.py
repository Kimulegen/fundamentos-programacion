#! Python
# Geometry calculator

import math

print("Calculadora geométrica")

# menu
while True:
    print(" Menú ".center(30, "="))
    print("1. Calcular Perímetro")
    print("2. Calcular Área")
    print("3. Salir")
    menu_option = int(input("Elija una opción: "))
    print()

    # perimeter calculator
    if menu_option == 1:
        while True:
            print("Calcular Perímetro")
            print("1. Para Círculo")
            print("2. Para Rectángulo")
            print("3. Para Cuadrado")
            print("4. Volver menu principal")
            perim_option = int(input("Elija una opción: "))
            if perim_option == 1:
                radius = int(input("Ingrese el radio del círculo: "))
                perim = 2 * math.pi * radius
                print(f"El perímetro del círculo es: {perim}")
                print()
            elif perim_option == 2:
                length = int(input("Ingrese el largo del rectángulo: "))
                width = int(input("Ingrese el ancho del rectángulo: "))
                perim = 2 * length + 2 * width
                print(f"El perímetro del rectángulo es: {perim}")
                print()
            elif perim_option == 3:
                side = int(input("Ingrese el lado del cuadrado: "))
                perim = 4 * side
                print(f"El perímetro del cuadrado es: {perim}")
                print()
            elif perim_option == 4:
                break
            else:
                print("Opción no válida")

    # area calculator
    elif menu_option == 2:
        while True:
            print("Calcular Área")
            print("1. Para Círculo")
            print("2. Para Rectángulo")
            print("3. Para Cuadrado")
            print("4. Volver menu principal")
            area_option = int(input("Elija una opción: "))
            if area_option == 1:
                radius = int(input("Ingrese el radio del círculo: "))
                area = math.pi * pow(radius, 2)
                print(f"El área del círculo es: {area}")
                print()
            elif area_option == 2:
                length = int(input("Ingrese el largo del rectángulo: "))
                width = int(input("Ingrese el ancho del rectángulo: "))
                area = length * width
                print(f"El área del rectángulo es: {area}")
                print()
            elif area_option == 3:
                side = int(input("Ingrese el lado del cuadrado: "))
                area = pow(side, 2)
                print(f"El área del cuadrado es: {area}")
                print()
            elif area_option == 4:
                break
            else:
                print("Opción no válida")

    # exit menu
    elif menu_option == 3:
        print("adiós")
        break

    # handle invalid options
    else:
        print("Opción no válida")
