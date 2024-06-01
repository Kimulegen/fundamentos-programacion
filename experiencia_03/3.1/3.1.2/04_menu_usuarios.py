import os

users = {}
while True:
    print(' Menú '.center(30, "="))
    print('1. Iniciar sesión')
    print('2. Registrar usuario')
    print('3. Eliminar usuario')
    print('4. Salir')
    choice = input('> ')

    if choice == '1':
        user = input('Ingrese su usuario\n> ')
        if user not in users:

            os.system('cls||clear')
            print('No hay usuarios registrados con ese nombre\n')

            continue
        psswrd = input('Ingrese su contraña\n> ')
        if users[user] != psswrd:

            os.system('cls||clear')
            print('Contraseña incorrecta\n')

            continue

        os.system('cls||clear')
        print(f'Bienvenido {user}\n')

    elif choice == '2':
        print('Registro de usuario')
        user = input('usuario: ')
        psswrd = input('contraseña: ')
        if user in users:
            print('ya existe el usuario con ese nombre')
            continue
        users[user] = psswrd

        os.system('cls||clear')
        print('Usuario registrado con éxito\n')

    elif choice == '3':
        user = input('Ingrese el usuario a eliminar\n> ')
        if user not in users:
            print('No hay usuarios registrados con ese nombre')
            continue
        psswrd = input('Confirme la eliminación ingresando contraseña\n> ')
        if users[user] != psswrd:

            os.system('cls||clear')
            print('Contraseña incorrecta\n')

            continue
        del users[user]

        os.system('cls||clear')
        print('Usuario eliminado con éxito\n')

    elif choice == '4':
        break

    else: 
        os.system('cls||clear')
        print("Error, opción inválida\n")
