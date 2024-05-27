while True:
    try:
        edad = int(input("Ingrese su edad\n> "))
        if edad < 10 or edad > 80:
            print("La edad está fuera del rango permitido, favor ingresar su edad denuevo\n")
            continue
    except ValueError:
        print("El dato ingresado no es un número entero, favor ingresar su edad denuevo\n")
    else:
        break
