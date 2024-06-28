#! python3
# Guarda las notas y la asistencia de los estudiantes de un curso

# importamos librerias
import csv

# inicializamos variables
clase = []


# funcion que calcula la nota de presentacion al examen
def calcular_nota(p1, p2, p3):
    # solo necesitamos multiplicar las notas por su ponderacion (30% -> .30)
    # y sumarlas
    return (p1 * 0.30) + (p2 * 0.35) + (p3 * 0.35)


# funcion que calcula el porcentaje de asistencia
def aprobo_asistencia(asistencia):
    # primero hay que transformar los "numeros" de string a int
    asistencia_int = tuple(map(int, asistencia))

    # calcular el porcentaje de asistencia
    # sumar asistencia, dividira por el numero de dias y multplicarla por 100
    asistencia_porcentaje = (sum(asistencia_int) / 5) * 100

    # calcular si el estudiante aprueba o no
    if asistencia_porcentaje > 65:
        return True
    else:
        return False


# funcion que guarda la asistencia
def guardar_clase(nombre_archivo, clase):
    # asumimos que clase es una lista de estudiantes, cada estudiante es un string
    # de la forma OSCAR ANTONIO BADILLA AGUILERA,45,48,68,1,1,1,0,1,0,1

    # abrimos el archivo en modo escritura,
    # usamos el escritor de archivos csv "writer"
    with open(
        f"{nombre_archivo}.csv", "w", encoding="utf-8", newline=""
    ) as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)

        # escribimos los encabezados
        escritor_csv.writerow(
            ["Nombre", "p1", "p2", "p3", "11", "a2", "a3", "a4", "a5"]
        )

        # escribimos la informacion de la clase
        for estudiante in clase:
            escritor_csv.writerow(estudiante.split(","))

    print("Archivo guardado con éxito")


# funcion que calcular el promedio de la clase
def calcular_promedio_clase(nombre_archivo):
    # abrimos el archivo en modo lectura
    # usamos el lector de archivos csv "reader"
    with open(f"{nombre_archivo}.csv", "r", encoding="utf-8") as archivo_csv:
        # inicializamos variables
        suma_promedios = 0
        numero_estudiantes = 0

        lector_csv = csv.reader(archivo_csv)

        # manejamos los datos
        for index, estudiante in enumerate(lector_csv):
            # si estamos leyendo el encabezado, saltalo
            if index == 0:
                continue

            # sacamos las notas de cada estudiante
            # convertimos las notas a int
            notas_int = tuple(map(int, estudiante[1:4]))

            # vamos sumando los promedios de cada estudiante
            suma_promedios += calcular_nota(*notas_int)
            numero_estudiantes += 1

        # calculamos el promedio de la clase al dividir suma_promedios
        # por el numero de estudiantes
        promedio_clase = suma_promedios / numero_estudiantes

        return promedio_clase


# menu principal
def main():
    while True:
        print(" Menu ".center(30, "="))
        print("1. Añadir estudiante")
        print("2. Guardar clase")
        print("3. Obtener promedio clase")
        print("4. Ver si un estudiante aprobo por asistencia")
        print("5. Salir")

        # leer la opcion del usuario, si no ingresa un numero o si
        # ingresa un numero fuera de rango tira un error
        try:
            opcion = int(input("\nIngresa una opción\n> "))
            if opcion < 1 or opcion > 5:
                raise ValueError
        except ValueError:
            print("\nOpción no válida\n")
            continue

        # añadir un estudiante a la clase
        if opcion == 1:
            estudiante = input("Ingresa la información del estudiante\n> ")
            clase.append(estudiante)

        # guardar la clase a un archivo
        elif opcion == 2:
            nombre_archivo = input("Ingresa el nombre del archivo a guardar\n> ")
            guardar_clase(nombre_archivo, clase)

        # obtener el promedio de la clase
        elif opcion == 3:
            nombre_archivo = input("Ingresa el nombre del archivo a leer\n> ")
            promedio = calcular_promedio_clase(nombre_archivo)
            print(f"El promedio de la clase es {promedio}")

        # buscar un estudiante y comprobar si aprobó o no por asistencia
        elif opcion == 4:
            nombre_archivo = input("Ingresa el nombre del archivo a leer\n> ")
            nombre_estudiante = input("Ingresa el nombre del estudiante a buscar\n> ")

            # leemos el archivo
            with open(f"{nombre_archivo}.csv", "r") as csv_archivo:
                lector_csv = csv.reader(csv_archivo)

                # buscamos el estudiante
                estudiante = [
                    estudiante
                    for estudiante in lector_csv
                    if estudiante[0] == nombre_estudiante
                ]

                # comprobamos si existe el estudiante en la clase o no
                if not len(estudiante):
                    print("No se encontró un estudiante con ese nombre")

                # si existe el estudiante calcula si el estudiante aprobó
                # sacando la información de la asistencia de la lista
                else:
                    if aprobo_asistencia(estudiante[0][4:]):
                        print("El estudiante aprobó por asistencia")
                    else:
                        print("El estudiante reprobó por asistencia")

        # salir del programa
        else:
            print("Saliendo del programa...")
            break


if __name__ == "__main__":
    main()
