#! Python3
# Create a supermarket list

import sys
import os

# intitlize variables
sw = 1
listaSuper = []
valorSuper = []


print("Presiones 1 para ingresar los productos del súper")
print("Presione cualquier tecla para salir")

# handle error in case user inputs a non integer value
try:
    op = int(input("Seleccione opción\n> "))
except ValueError:
    print("Adiós")
    sys.exit()

# menu
if op == 1:
    while sw == 1:
        # handle error in case price is not an integer
        try:
            print("-" * 50)
            producto = input("Incorpore su producto, para salir, presione 0:\n> ")
            if producto != "0":
                # append values to corresponding lists
                valorSuper.append(int(input(f"Incorpore el valor de {producto}\n> ")))
                listaSuper.append(producto)
                os.system("cls||clear")
                # print cart
                print(" DETALLE BOLETA ".center(50, "="))
                print(f"Productos comprados: {', '.join(listaSuper)}")
                print(f"Cantidad de productos comprados: {len(listaSuper)}")
                print(f"Suma de todos los productos: {sum(valorSuper)}")
            else:
                print("Adiós")
                sw = 0
        except ValueError:
            os.system("cls||clear")
            print("Valor del producto no válido")
else:
    print("Adiós")
