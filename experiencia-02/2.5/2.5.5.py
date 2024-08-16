#! Python3
# User sign in and sign up

import pwinput
import re
from time import sleep

# inititlize variables
user1 = None
user2 = None
user3 = None
pwd1 = None
pwd2 = None
pwd3 = None
number_or_users = 0


# define functions to check phone and email formats
def is_phone_formatted(phone):
    return phone[0] == "9" and len(phone) == 9


def is_email_formatted(email):
    return not not re.search(r"^\w+@\w+\.(com|net|cl)$", email)


# menu
while True:
    print(" Menú ".center(30, "="))
    print("1. Iniciar sesion")
    print("2. Registrar usuario")
    print("3. Salir")
    try:
        opt = int(input("Seleccione una opcion:\n> "))

    # handle exceptions
    except ValueError as ve:
        print("Opcion numerica invalida, saliendo del programa")
        break

    # Sign in
    if opt == 1:
        if number_or_users == 0:
            print("\nNo hay usuarios registrados\n")
            continue

        user = input("Ingrese su usuario\n> ")
        pwd = pwinput.pwinput("Ingrese su contrasena\n> ")

        if (
            (user == user1 and pwd == pwd1)
            or (user == user2 and pwd == pwd2)
            or (user == user3 and pwd == pwd3)
        ):
            print(f"\nBienvenido {user}\n")
            while True:
                print(" Menú 2".center(30, "="))
                print("1. Realizar llamada")
                print("2. Enviar correo electronico")
                print("3. Cerrar sesion")
                try:
                    inner_opt = int(input("Seleccione una opcion:\n> "))

                # handle exceptions
                except ValueError as ve:
                    print("Opcion numerica invalida saliendo del menu")
                    break

                # make phone calls
                if inner_opt == 1:
                    while True:
                        phone = input(
                            "Ingrese numero telefonico a llamar  (Ingrese 0 para volver)\n> "
                        )
                        if phone == "0":
                            break
                        if is_phone_formatted(phone):
                            print("Realizando llamada...\n")
                            sleep(1)
                            break
                        else:
                            print(
                                "\nFormato del telefono ingresado invalido.\nEl telefono debe empezar con un 9 y tener 9 digitos.\n"
                            )

                # send emails
                if inner_opt == 2:
                    while True:
                        email = input(
                            "Ingrese la direccion de correo a la cual desea enviar (Ingrese 0 para volver)\n> "
                        )
                        if email == "0":
                            break
                        elif is_email_formatted(email):
                            message = input("Ingrese mensaje a enviar\n> ")
                            print("Enviando mensaje...\n")
                            sleep(1)
                            break
                        else:
                            print(
                                "\nFormato de correo invalido. Favor ingresar un correo valido\n"
                            )

                # log out
                if inner_opt == 3:
                    print("Cerrando sesion...\n")
                    sleep(1)
                    break
        else:
            print("\nUsuario o contrasena incorrectos!!!\n")

    # Sign up
    elif opt == 2:
        user_to_register = input("Ingrese su nombre de usuario\n> ")
        pwd_to_register = pwinput.pwinput("Ingrese su contrasena\n> ")

        if user1 is None:
            user1, pwd1 = user_to_register, pwd_to_register
            number_or_users += 1
            print("\nUsuario registrado con exito\n")
        elif user2 is None:
            user2, pwd2 = user_to_register, pwd_to_register
            number_or_users += 1
            print("\nUsuario registrado con exito\n")
        elif user3 is None:
            user3, pwd3 = user_to_register, pwd_to_register
            number_or_users += 1
            print("\nUsuario registrado con exito!!!\n")
        else:
            print("\nNo se pueden registrar mas usuarios!!!\n")
            continue

    # exit menu
    elif opt == 3:
        print("\nSaliendo del programa...")
        sleep(1)
        break

    # handle invalid inputs
    else:
        print("\nOpcion invalida!!!\n")
