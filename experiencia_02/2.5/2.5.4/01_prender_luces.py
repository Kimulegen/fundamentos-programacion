luces_patio = luces_sala = luces_pasillo = luces_jardin = False
sw = 1

while sw == 1:
    print("1.- Encender/Apagar luces Patio (Alternado)")
    print("2.- Encender/Apagar luces Sala (Alternado)")
    print("3.- Encender/Apagar luces Pasillo (Alternado)")
    print("4.- Encender/Apagar luces Jardín (Alternado)")
    print("5.- Encender todo (Alternado)")
    print("6.- Apagar todo (Alternado)")
    print("1.- Salir del sistema")

    try:
        opt = int(input("Ingrese la opción deseada: "))
    except ValueError as ve:
        print(ve)
        print("Error en la selección de la opción")
    else:
        if opt == 1:
            luces_patio = not luces_patio
            
            if luces_patio:
                print("El patio está encendido")
            else:
                print("El patio está apagado")
        elif opt == 2:
            luces_sala = not luces_sala
            
            if luces_sala:
                print("La sala está encendido")
            else:
                print("La sala está apagado")
        elif opt == 3:
            luces_pasillo = not luces_pasillo
            
            if luces_pasillo:
                print("El pasillo está encendido")
            else:
                print("El pasillo está apagado")
        elif opt == 4:
            luces_jardin = not luces_jardin
            
            if luces_jardin:
                print("El jardín está encendido")
            else:
                print("El jardín está apagado")
        elif opt == 5:
            luces_patio = luces_sala = luces_pasillo = luces_jardin = True
            print("Todas las luces están encendidas")
        elif opt == 6:
            luces_patio = luces_sala = luces_pasillo = luces_jardin = False
            print("Todas las luces están apagadas")
        elif opt == 7:
            print("Hasta pronto...")
            sw = 0
        else: 
            print("Opción no válida")