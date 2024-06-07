#! Python3
# Validate user name and password

user = input("Ingrese su user")
pwd = input("Ingrese su pass")

if user == "user" and pwd == "password":
    print("Bienvenido")
else:
    print("Error en contraseña")
