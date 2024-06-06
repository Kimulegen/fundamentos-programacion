#! Python3
# Calculate grade point average

# importing os for clear
import os
# importin sys to exit program
import sys

# initializa variables
sw = 1
listaNotas = []

# menu
print("Presione 1 para ingresar sus notas")
print("Presione cualquier tecla para salir")

try:
    op = int(input("Seleccione su opción\n> "))
except ValueError:
    print("Adiós")
    sys.exit()

if (op == 1):
    while sw == 1:
        try:
            print("---------------------------------------------------------")
            nota = int(input("Incorpore su nota, si desea salir, presione 0:"))
            if (nota != 0):
                listaNotas.append(nota)
                print('Notas ingresadas hasta ahora: ', " ".join(map(str,listaNotas)))
                print("Cantidad de notas ingresadas: ", len(listaNotas))
                promedioNotas = sum(listaNotas) / len(listaNotas)
                print(f"Promedio de notas: {promedioNotas:.{2}f}")
            else:
                print("Adiós")
                sw == 0
        except ValueError as ve:
            print(ve)
            print("Ingreso Erróneo")
else:
    print("Adiós")
