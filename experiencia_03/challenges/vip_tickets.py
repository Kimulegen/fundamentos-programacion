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
attendees = []


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


def is_valid(rut_str):
    if rut_str[0] == "0":
        return False

    if len(rut_str) < 7 or len(rut_str) > 8:
        return False

    try:
        int(rut_str)
    except ValueError:
        return False

    return True


def calculate_total_profits(seats):
    profits = 0
    tickets_sold = {"platinum": 0, "gold": 0, "silver": 0}
    for index, seat in enumerate(seats):
        if isinstance(seat, str):
            if index <= 19:
                tickets_sold["platinum"] = tickets_sold["platinum"] + 1
                profits = profits + 120000
            elif index <= 49:
                tickets_sold["gold"] = tickets_sold["gold"] + 1
                profits = profits + 80000
            else:
                tickets_sold["silver"] = tickets_sold["silver"] + 1
                profits = profits + 50000

    print("-" * 54)
    print(
        "Tipo de Entrada".center(20, " "),
        "|",
        "Cantidad".center(10, " "),
        "|",
        "Total".center(20, " "),
    ), print("-" * 54),
    print(
        "Platinum $120.000".ljust(20, " "),
        "|",
        f'{tickets_sold["platinum"]}'.center(10, " "),
        "|",
        f'${tickets_sold["platinum"]*120000}'.center(20, " "),
    ), print("-" * 54),
    print(
        "Gold $80.000".ljust(20, " "),
        "|",
        f'{tickets_sold["gold"]}'.center(10, " "),
        "|",
        f'${tickets_sold["gold"]*8000}'.center(20, " "),
    ), print("-" * 54),
    print(
        "Silver $50.000".ljust(20, " "),
        "|",
        f'{tickets_sold["silver"]}'.center(10, " "),
        "|",
        f'${tickets_sold["silver"]*50000}'.center(20, " "),
    ), print("-" * 54),
    print(
        "Total.".ljust(20, " "),
        "|",
        f'{tickets_sold["platinum"]+tickets_sold["gold"]+tickets_sold["silver"]}'.center(
            10, " "
        ),
        "|",
        f'${tickets_sold["platinum"]*120000 + tickets_sold["gold"]*8000+tickets_sold["silver"]*50000} '.center(
            20, " "
        ),
    ), print("-" * 54), print()


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
                            "Ingresa el rut de la persona que va a utilizar ese asiento\nSin digito verificador\n> "
                        )

                        while not is_valid(rut):
                            rut = input("ingresa un rut valido: ")
                        seats[seat_to_buy - 1] = rut
                        attendees.append(int(rut))
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
            display_seats(seats)
        elif choice == 3:
            print("Lista de asistentes")
            print("-" * 20)
            attendees.sort()
            for attendee in attendees:
                print(attendee)
        elif choice == 4:
            calculate_total_profits(seats)
        else:
            print("Saliendo del programa...")
            break


if __name__ == "__main__":
    os.system("cls||clear")
    main()
