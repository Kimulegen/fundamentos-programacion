canasta = {}
total = 0
while True:
    print('*'*15, 'Menú', '*'*15)
    print('1. Agregar productos')
    print('2. Ver canasta')
    print('3. Ver total')
    print('4. Salir')
    choice = input('> ')
    print()

    if choice == '1':
        print('Seleccione producto a agregar')
        print('1. Arroz $2350')
        print('2. Tallarines $1190')
        print('3. Aceite $2290')
        print('4. Mermelada $1450')
        print('5. Cereal $2690')
        product = input('> ')
        print()

        if product == '1':
            canasta.setdefault('arroz', 0)
            canasta['arroz'] += 1
            total += 2350
        elif product == '2':
            canasta.setdefault('tallarines', 0)
            canasta['tallarines'] += 1
            total += 1190
        elif product == '3':
            canasta.setdefault('aceite', 0)
            canasta['aceite'] += 1
            total += 2290
        if product == '4':
            canasta.setdefault('mermelada', 0)
            canasta['mermelada'] += 1
            total += 1450
        if product == '5':
            canasta.setdefault('cereal', 0)
            canasta['cereal'] += 1
            total += 2690
        
    elif choice == '2':
        for k,v in canasta.items():
            print(f'{v} {k}')
        print()
    elif choice == '3':
        print(f'Su total a pagar es: {total}')
        print()
    elif choice == '4':
        break
