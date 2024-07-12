import random
import csv
import os

trabajadores = [
    {"nombre": "Juan Pérez", "cargo": "Consultor TI"},
    {"nombre": "María García", "cargo": "Analista"},
    {"nombre": "Carlos López", "cargo": "Programador"},
    {"nombre": "Ana Martínez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Pedro Rodríguez", "cargo": "Consultor TI"},
    {"nombre": "Laura Hernández", "cargo": "Analista"},
    {"nombre": "Miguel Sánchez", "cargo": "Programador"},
    {"nombre": "Isabel Gómez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Francisco Díaz", "cargo": "Consultor TI"},
    {"nombre": "Elena Fernández", "cargo": "Analista"},
]


def asignar_sueldos_aleatorios(trabajadores):
    for trabajador in trabajadores:
        trabajador.update({"sueldo": random.randrange(300_000, 2_600_000, 100_000)})

    print("\nSueldo asignados con exito\n")


def clasificar_sueldos(trabajadores):
    sueldo_bajo = []
    sueldo_medio = []
    sueldo_alto = []

    for trabajador in trabajadores:
        if trabajador["sueldo"] < 800_000:
            sueldo_bajo.append(trabajador)
        elif trabajador["sueldo"] <= 2_000_000:
            sueldo_medio.append(trabajador)
        else:
            sueldo_alto.append(trabajador)

    # Se puede mejorar
    print(f"Sueldos menores a $800.000 TOTAL: {len(sueldo_bajo)}")
    print("Nombre empleado\t\tCargo\t\t\tSueldo")
    for trabajador in sueldo_bajo:
        if trabajador["cargo"] == "Jefe de Proyecto":
            print(
                f'{trabajador["nombre"]}\t\t{trabajador["cargo"]}        ${trabajador["sueldo"]}'
            )
        else:
            print(
                f'{trabajador["nombre"]}\t\t{trabajador["cargo"]}\t\t${trabajador["sueldo"]}'
            )
    print("")

    print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {len(sueldo_medio)}")
    print("Nombre empleado\t\tCargo\t\t\tSueldo")
    for trabajador in sueldo_medio:
        if trabajador["cargo"] == "Jefe de Proyecto":
            print(
                f'{trabajador["nombre"]}\t\t{trabajador["cargo"]}        ${trabajador["sueldo"]}'
            )
        else:
            print(
                f'{trabajador["nombre"]}\t\t{trabajador["cargo"]}\t\t${trabajador["sueldo"]}'
            )
    print("")

    print(f"Sueldos superioresa $2.000.000 TOTAL: {len(sueldo_alto)}")
    print("Nombre empleado\t\tCargo\t\t\tSueldo")
    for trabajador in sueldo_alto:
        if trabajador["cargo"] == "Jefe de Proyecto":
            print(
                f'{trabajador["nombre"]}\t\t{trabajador["cargo"]}        ${trabajador["sueldo"]}'
            )
        else:
            print(
                f'{trabajador["nombre"]}\t\t{trabajador["cargo"]}\t\t${trabajador["sueldo"]}'
            )
    print("")

    total_sueldo = 0
    for trabajador in trabajadores:
        total_sueldo += trabajador["sueldo"]

    print(f"TOTAL SUELDOS: ${total_sueldo}\n")


def ver_estadisticas(trabajadores):
    lista_sueldos = []
    suma_sueldos = 0
    mult_sueldos = 1
    for trabajador in trabajadores:
        lista_sueldos.append(trabajador["sueldo"])
        suma_sueldos += trabajador["sueldo"]
        mult_sueldos *= trabajador["sueldo"]

    print("Sueldo mas alto:", max(lista_sueldos))
    print("Sueldo mas bajo:", min(lista_sueldos))
    print("Promedio de sueldos:", suma_sueldos)
    print("Media geometrica de sueldos:", mult_sueldos ** (1 / len(lista_sueldos)))
    print()


def generar_reporte_sueldos(trabajadores):
    descuento_salud = 0.7
    descuento_afp = 0.12

    for trabajador in trabajadores:
        desc_salud = round(trabajador["sueldo"] * descuento_salud)
        desc_afp = round(trabajador["sueldo"] * descuento_afp)
        sueldo_liquido = trabajador["sueldo"] - (desc_salud + desc_afp)
        trabajador.update(
            {
                "descuento_salud": desc_salud,
                "descuento_afp": desc_afp,
                "sueldo_liquido": sueldo_liquido,
            }
        )

    print(
        "Nombre empleado\t\tCargo\t\t\tSueldo Base\t\tDescuento Salud\t\tDescuento AFP\t\t Sueldo Liquido"
    )
    for trabajador in trabajadores:
        if trabajador["cargo"] == "Jefe de Proyecto":
            print(
                f'{trabajador["nombre"]}\t\t{trabajador["cargo"]}        ${trabajador["sueldo"]}\t\t${trabajador["descuento_salud"]}\t\t${trabajador["descuento_afp"]}\t\t\t${trabajador["sueldo_liquido"]}'
            )
        else:
            print(
                f'{trabajador["nombre"]}\t\t{trabajador["cargo"]}\t\t${trabajador["sueldo"]}\t\t${trabajador["descuento_salud"]}\t\t${trabajador["descuento_afp"]}\t\t\t${trabajador["sueldo_liquido"]}'
            )

    with open(
        "planilla_trabajadores.csv", "w", newline="", encoding="utf-8"
    ) as csv_file:
        fieldnames = [
            "nombre",
            "cargo",
            "sueldo",
            "descuento_salud",
            "descuento_afp",
            "sueldo_liquido",
        ]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(trabajadores)
        print("\nArchivo creado con exito\n")


def main():
    while True:
        print(" Menu ".center(30, "="))
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadisticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir del programa")
        try:
            op = int(input("> "))
            if not (0 <= op <= 5):
                raise ValueError
        except ValueError:
            os.system("cls||clear")
            print("\nOpcion invalida\n")
            continue

        os.system("cls||clear")
        if op == 0:
            print(trabajadores)
        if op == 1:
            asignar_sueldos_aleatorios(trabajadores)
        if op == 2:
            clasificar_sueldos(trabajadores)
        if op == 3:
            ver_estadisticas(trabajadores)
        if op == 4:
            generar_reporte_sueldos(trabajadores)
        if op == 5:
            print("Finalizando programa...")
            print("Desarrollado por Kimulegen")
            print("RUT 11.111.111")
            break


if __name__ == "__main__":
    os.system("cls||clear")
    main()
