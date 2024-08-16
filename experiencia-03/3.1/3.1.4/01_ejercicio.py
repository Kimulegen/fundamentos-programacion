#! Python3
# Calculate grade point average

import os

# importin sys to exit program
import sys

# initialize variables
sw = 1
listaNotas = []

# menu
print("Presione 1 para ingresar sus notas")
print("Presione cualquier tecla para salir")

# ask for user input
# handle error in case user input is not a number
try:
    op = int(input("Seleccione su opción\n> "))
except ValueError:
    print("Adiós")
    sys.exit()

if op == 1:
    # ask for grades until user press 0
    os.system("cls||clear")
    while sw == 1:
        # handle error in case user input is not a number
        try:
            print("=" * 50)
            nota = int(input("Incorpore su nota, si desea salir, presione 0:\n> "))

            # if user enters a grade, show grades list, number of grades, and the average
            if nota != 0:
                os.system("cls||clear")
                listaNotas.append(nota)
                print("Notas ingresadas hasta ahora: ", " ".join(map(str, listaNotas)))
                print("Cantidad de notas ingresadas: ", len(listaNotas))
                promedioNotas = sum(listaNotas) / len(listaNotas)
                print(f"Promedio de notas: {promedioNotas:.{2}f}")
            else:
                print("Adiós")
                sw = 0
        except ValueError as ve:
            print(ve)
            print("Ingreso Erróneo")
else:
    print("Adiós")
