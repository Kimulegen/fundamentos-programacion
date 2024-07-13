#! python3
# Register employees, calculate liquid salary

import os

employees = []


def register_employee():
    employee = {}
    while True:
        name = input("Ingresa el nombre del trabajador: ")
        lastname = input("Ingresa el apellido del trabajador: ")
        position = input("Ingresa el cargo del trabajador: ")
        while True:
            try:
                gross_salary = int(input("Ingresa el sueldo bruto: "))
                if gross_salary < 0:
                    raise ValueError
                break
            except ValueError:
                print("monto ingresado no valido")
        if name == "" or lastname == "" or position == "" or gross_salary == "":
            print("Te falto ingresar un dato")
        else:
            break

    health_disc = int(gross_salary * 0.7)
    afp_disc = int(gross_salary * 0.12)
    liquid_salary = gross_salary - health_disc - afp_disc
    employee["name"] = name
    employee["lastname"] = lastname
    employee["position"] = position
    employee["gross_salary"] = gross_salary
    employee["health_disc"] = health_disc
    employee["afp_disc"] = afp_disc
    employee["liquid_salary"] = liquid_salary

    employees.append(employee)
    os.system("cls||clear")
    print("usuario registrado con exito\n")


def list_employees():
    print("Trabajador\tCargo\tSueldoBruto\tDesc. Salud\tDesc. AFP\tLiquido a pagar")
    for employee in employees:
        print(employee["name"], employee["lastname"], end="\t")
        print(employee["position"], end="\t")
        print(employee["gross_salary"], end="\t")
        print(employee["health_disc"], end="\t")
        print(employee["afp_disc"], end="\t")
        print(employee["liquid_salary"], end="\n")


def print_spreadsheet(employee_list):
    with open(
        "planilla_sueldos.txt",
        "w",
        encoding="utf-8",
        newline="",
    ) as txt:
        txt.write(
            "Trabajador\tCargo\tSueldo Bruto\tDesc. Salud\tDesc. AFP\tLiquido a pagar\n"
        )
        for employee in employee_list:
            txt.write(f'{employee["name"]} ')
            txt.write(employee["lastname"])
            txt.write("\t")
            txt.write(employee["position"])
            txt.write("\t")
            txt.write(str(employee["gross_salary"]))
            txt.write("\t")
            txt.write(str(employee["health_disc"]))
            txt.write("\t")
            txt.write(str(employee["afp_disc"]))
            txt.write("\t")
            txt.write(str(employee["liquid_salary"]))
            txt.write("\n")

        print("Archivo guardado con exito")


e_l = [
    {
        "name": "Oscar",
        "lastname": "Munoz",
        "position": "CEO",
        "gross_salary": 100000,
        "liquid_salary": 80000,
    },
    {
        "name": "Andres",
        "lastname": "Santelices",
        "position": "Dev",
        "gross_salary": 1330000,
        "liquid_salary": 8000,
    },
]


def main():
    while True:
        print(" Menu ".center(40, "="))
        print("1. Registrar trabajador")
        print("2. Listar a todos los trabajadores")
        print("3. Imprimir planilla de sueldos")
        print("4. Salir")

        try:
            opt = int(input("\nIngrese su opcion\n> "))
            if opt < 1 or opt > 4:
                raise ValueError
        except ValueError:
            os.system("cls||clear")
            print("Opcion no valida\n")
            continue

        os.system("cls||clear")
        if opt == 1:
            register_employee()
        elif opt == 2:
            list_employees()
        elif opt == 3:
            position_filter = input(
                "Ingresa el cargo por el cual quieres filtrar los trabajadores,\n presiona Enter para imprimir a todos los trabajadores\n> "
            )
            os.system("cls||clear")
            if position_filter != "":
                filtered = [
                    emp for emp in employees if emp["position"] == position_filter
                ]
            else:
                filtered = employees
            print_spreadsheet(filtered)
        else:
            print("Saliendo del programa...")
            break


if __name__ == "__main__":
    os.system("cls||clear")
    main()
