# EJERCICIO 1
# Descuento por edad
edad = int(input("Ingrese su edad"))

if edad > 0 and edad < 18:
    print(f"Edad: {edad}, tiene un descuento de un 50%")
elif edad >= 18 and edad < 30:
    print(f"Edad: {edad}, tiene un descuento de un 20%")
elif edad >= 60:
    print(f"Edad: {edad}, tiene un descuento de un 90%")
else:
    print(f"Edad: {edad}, no aplica descuento")

# EJERCICIO 2
# Validación user y pass
user = input("Ingrese su user")
pwd = input("Ingrese su pass")

if user=="user" and pwd=="password":
    print("Bienvenido")
else:
    print("Error en contraseña")

# EJERCICIO 3
user = input("Ingrese su user")
pwd = input("Ingrese su pass")

if user=="duoc" and pwd=="123duoc":
    valorDev = int(input("Bienvenido, ingrese el valor a devolver: ")
    if valorDev > 100000:
        print("Se dará la máxima urgencia a su devolución de dinero")
    else: 
        print("El caso ha quedado registrado, le informaremos lo antes posible")
else:
    print("Error en contraseña")

# ¿Qué mensaje nos imprimirá el sistema, si nos devuelve una devolución de dinero de $120.000, e ingresamos el user "duoc123" y el pass "123duoc"?
# R: Error en contraseña
