#! Python3
# Generate, show, and save a car log

import os
import csv
from datetime import datetime

# initialize variables
bitacora = []


# menu
def main():
    while True:
        print(" Bienvenido al menú, seleccione su opción ".center(60, "="))
        print("1. Agregar acción")
        print("2. Ver bitácora")
        print("3. Guardar bitácora")
        print("4. Salir")
        try:
            choice = int(input("> "))
        except ValueError:
            os.system("cls||clear")
            print("\nError, favor ingrese un dato numérico\n")
            continue

        print()

        # add an entry to the log
        if choice == 1:
            os.system("cls||clear")
            action = input("¿Qué acción desea agregar?\n> ")
            formatted_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            bitacora.append([formatted_datetime, action])
            os.system("cls||clear")
            print("Acción agregada")

        # show car log
        elif choice == 2:
            os.system("cls||clear")
            print(" Bitácora del auto ".center(60, "="))
            if len(bitacora) == 0:
                print("No hay acciones registradas por el momento")
            else:
                for fecha, action in bitacora:
                    print(fecha, action)

        # save car log to csv file
        elif choice == 3:
            os.system("cls||clear")
            file_name = input(
                "Ingrese el nombre del archivo al cual desea guardar la bitácora\n> "
            )
            file_name = file_name if len(file_name) > 0 else "bitacora"
            fieldnames = ["fecha", "accion"]
            with open(
                f"{file_name}.csv", "w+", newline="", encoding="utf-8"
            ) as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(
                    {"fecha": action[0], "accion": action[1]} for action in bitacora
                )
                os.system("cls||clear")
                print("Bitácora guardada con éxito")

        # exit program
        elif choice == 4:
            print("Saliendo del menú")
            break

        # handle invalid options
        else:
            os.system("cls||clear")
            print("\nFavor ingresar una opción válida\n")
        print()


if __name__ == "__main__":
    main()
