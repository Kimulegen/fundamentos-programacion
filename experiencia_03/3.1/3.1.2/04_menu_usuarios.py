users = {}
while True:
    print('*'*15, 'Menú', '*'*15)
    print('1. Iniciar sesión')
    print('2. Registrar usuario')
    print('3. Eliminar usuario')
    print('4. Salir')
    choice = input('> ')

    if choice == '1':
        user = input('Ingrese su usuario\n> ')
        if user not in users:
            print('No hay usuarios registrados con ese nombre')
            continue
        psswrd = input('Ingrese su contraña\n> ')
        if users[user] != psswrd:
            print('Contraseña incorrecta')
            continue

        print(f'Bienvenido {user}')

    elif choice == '2':
        print('Registro de usuario')
        user = input('usuario: ')
        psswrd = input('contraseña: ')
        if user in users:
            print('ya existe el usuario con ese nombre')
            continue
        users[user] = psswrd

        print('Usuario registrado con éxito')

    elif choice == '3':
        user = input('Ingrese el usuario a eliminar\n> ')
        if user not in users:
            print('No hay usuarios registrados con ese nombre')
            continue
        psswrd = input('Confirme la eliminación ingresando contraseña\n> ')
        if users[user] != psswrd:
            print('Contraseña incorrecta')
            continue
        del users[user]
        print('Usuario eliminado con éxito')

    elif choice == '4':
        break