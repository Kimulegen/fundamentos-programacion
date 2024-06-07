#! Python3
# Ask for user info, validate that user

user = input("Ingrese su usario")
pwd = input("Ingrese su contraseña")

if (user == "pedro" and pwd == "1234") or (user == "angel" and pwd == "a4s1"):
    print("Bienvenido")
else:
    print("Usuario o contraseña incorrecto")
