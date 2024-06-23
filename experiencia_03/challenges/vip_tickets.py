#! python3
# Sell VIP tickets
"""
menu
comprar entradas
mostrar ubicaciones disponibles
ver listado de asistentes
mostrar ganancias totales

"""
import os

# initialize variables
seats = list(range(1, 101))


def sell_seat(seats, seat_number, rut):
    if len(seats[seat_number - 1]) > 2:
        print("No disponible")
        return False
    else:
        seats[seat_number - 1] = rut
    return True


def display_seats(seats):
    print("-" * 29)
    print("|", "|".rjust(27, " "))
    print("|", "ESCENARIO".center(25, " "), "|")
    print("|", "|".rjust(27, " "))
    print("-" * 29)

    counter = 0
    for i in seats:
        if counter % 10 == 0:
            print()
        if isinstance(i, str):
            print("x".rjust(2, " "), end=" ")
        else:
            print(f"{i:02}", end=" ")
        counter += 1
    print("\n\n")


def main():
    while True:

        print(" Menu ".center(30, "="))
        print("1. Comprar entradas")
        print("2. Mostrar ubicaciones disponibles")
        print("3. Ver listado de asistentes")
        print("4. Mostrar ganancias totales")
        print("5. Salir")

        try:
            choice = int(input("Eliga una opcion\n> "))
            if choice < 1 or choice > 5:
                raise ValueError
        except ValueError:
            os.system("cls||clear")
            print("\nOpcion no valida\n")
            continue

        os.system("cls||clear")
        if choice == 1:
            while True:
                try:
                    n_of_tickets = int(
                        input(
                            "Ingrese el numero de entradas que desea comprar (1-3)\n> "
                        )
                    )
                    if n_of_tickets < 1 or n_of_tickets > 3:
                        raise ValueError
                    break
                except ValueError:
                    os.system("cls||clear")
                    print("\nNumero de entradas invalido\n")
                    continue

            purchase_summary = []
            for i in range(n_of_tickets):
                os.system("cls||clear")
                display_seats(seats)

                while True:
                    try:
                        seat_to_buy = int(input("Selecciona un asiento valido: "))
                        if seat_to_buy < 1 or seat_to_buy > 100:
                            raise ValueError
                    except ValueError:
                        print("Asiento no valido")
                        continue
                    if isinstance(seats[seat_to_buy - 1], str):
                        print("No esta disponible")
                    else:
                        rut = input(
                            "Ingresa el rut de la persona que va a utilizar ese asiento\n> "
                        )
                        seats[seat_to_buy - 1] = rut
                        purchase_summary.append({seat_to_buy: rut})
                        break

            os.system("cls||clear")
            print("Resumen de su compra:")
            print("-" * 21)
            for purchase in purchase_summary:
                for k, v in purchase.items():
                    k = f"{k:2}"
                    print(f"Usted compro la ubicacion {k} y lo asocio al rut {v}")
            print()

        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        else:
            print("Saliendo del programa...")
            break


if __name__ == "__main__":
    os.system("cls||clear")
    main()
