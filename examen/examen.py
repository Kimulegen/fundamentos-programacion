import random
import csv
import os

# DATA
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

# PROCESAR DATA
trabajadores_list = []
for trabajador in trabajadores:
    trabajadores_list.append({"nombre": trabajador, "sueldo": 0})

# 1. asignar sueldos
def asignar_suedos_aleatorios(trabajadores:list) -> None:
    for trabajador in trabajadores:
        trabajador.update({"sueldo": random.randrange(300_000,2_600_000, 100_000)})

    print("\n Sueldos asignados con éxito\n")

# 2. clasificar sueldos
def clasificar_sueldos(trabajadores:list) -> None:
    sueldo_bajo = [trabajador for trabajador in trabajadores if trabajador["sueldo"] < 800_000]
    sueldo_medio = [trabajador for trabajador in trabajadores if 800_000 <= trabajador["sueldo"] <= 2_000_000]
    sueldo_alto = [trabajador for trabajador in trabajadores if trabajador["sueldo"] > 2_000_000]

    def muestra_sueldos(mensaje:str, trabajadores:list) -> None:
        print(f"{mensaje} TOTAL: {len(trabajadores)}\n")
        if len(trabajadores) == 0:
            print("No hay trabajadores en el rango de sueldo especificado")
        else:
            print(f"Nombre empleado\tSueldo")
            for trabajador in trabajadores:
                print(f"{trabajador["nombre"]}\t${trabajador["sueldo"]}")
        print()

    muestra_sueldos("Sueldos menores a $800.000", sueldo_bajo)
    muestra_sueldos("Sueldos entre $800.000 y $2.000.000", sueldo_medio)
    muestra_sueldos("Sueldos superiores a $2.000.000", sueldo_alto)

# 3. ver estadisticas
def ver_estadisticas(trabajadores:list) -> None:
    sueldos = list(map(lambda tr: tr["sueldo"], trabajadores))
    max_sueldo = max(sueldos)
    min_sueldo = min(sueldos)
    prom_sueldos = sum(sueldos)//len(sueldos)
    mult_sueldos = 1

    for sueldo in sueldos:
        mult_sueldos *= sueldo
    
    print(f"Sueldo más alto:\t{max_sueldo}")
    print(f"Sueldo más bajo:\t{min_sueldo}")
    print(f"Promedio de sueldos:\t{prom_sueldos}")
    print(f"Media geométrica:\t{mult_sueldos**(1/len(sueldos))}")

# 4. reporte de sueldos
def generar_reporte(trabajadores:list) -> None:
    # muestra en pantalla información trabajadores
    def print_trabajadores(trabajadores:list) -> None:
        print("Nombre empleado".ljust(20),"Sueldo Base".ljust(20),"Descuento Salud".ljust(20),"Descuento AFP".ljust(20),"Sueldo Líquido".ljust(20))
        for trabajador in trabajadores:
            print(f"{trabajador["nombre"]}".ljust(20),f"${trabajador["sueldo"]}".ljust(20),f"${trabajador["descuento_salud"]}".ljust(20), f"${trabajador["descuento_afp"]}".ljust(20), f"${trabajador["sueldo_liquido"]}".ljust(20))

    # crea (o trunca) un archivo con la información de los trabajadores
    def crear_archivo(nombre_archivo:str, trabajadores:list) -> None:
        with open(f"{nombre_archivo}.csv", "w", newline="", encoding="utf-8") as archivo:
            fieldnames = ["nombre", "sueldo", "descuento_salud", "descuento_afp", "sueldo_liquido"]
            csv_writer = csv.DictWriter(archivo, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(trabajadores) 
        print("\nArchivo creado con éxito\n")

    DESC_SALUD = 0.7
    DESC_AFP = 0.12
    for trabajador in trabajadores:
        sueldo = trabajador["sueldo"]
        descuento_salud = round(sueldo * DESC_SALUD)
        descuento_afp = round(sueldo * DESC_AFP)
        sueldo_liquido = sueldo - (descuento_salud + descuento_afp)
        
        trabajador.update({"descuento_salud": descuento_salud, "descuento_afp": descuento_afp, "sueldo_liquido": sueldo_liquido})

    # side effect
    print_trabajadores(trabajadores)
    crear_archivo("planilla_trabajadores", trabajadores)


def main(trabajadores:list) -> None:
    while True:
        print(" Menu ".center(30, "="))
        print("1. Asignar sueldos")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        try: 
            op = int(input("> "))
            if not (1 <= op <= 5):
                raise ValueError
        except ValueError:
            os.system("cls||clear")
            print("\nOpción inválida\n")
            continue

        os.system("cls||clear")
        if op == 1:
            asignar_suedos_aleatorios(trabajadores)
        elif op == 2:
            clasificar_sueldos(trabajadores)
        elif op == 3:
            ver_estadisticas(trabajadores)
        elif op == 4:
            generar_reporte(trabajadores)
        else:
            print("Finalizando programa...")
            print("Desarrollado por Oscar Muñoz")
            print("RUT 18.295.080-7")
            break
        
if __name__ == "__main__":
    os.system("cls||clear")
    main(trabajadores_list)