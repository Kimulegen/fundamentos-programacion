# Ejercicio 1
age = int(nput("Ingrese su edad"))

if age < 18:
    print("eres menor de edad")
else:
    print("eres mayor de edad")

# Ejercicio 2
user = input("Ingrese su usario")
pwd = input("Ingrese su contraseña")

if (user == "pedro" and pwd == "1234") or (user == "angel" and pwd == "a4s1"):
    print("Bienvenido")
else: 
    print("Usuario o contraseña incorrecto")

# Ejercicio 3
nota1 = int(input("Ingrese la primera nota"))
nota2 = int(input("Ingrese la segunda nota"))
nota3 = int(input("Ingrese la tercera nota"))

promedio = (nota1 + nota2 + nota3) / 3

if promedio > 4.0:
    print("Aprobado")
else:
    print("Reprobado")

# Ejercicio 4
answer = input("¿Cuál de los siguientes animales vive en el agua? \nPerro\nCocodrilo\nConejo\nTiburón")
score = 0

if answer == "Cocodrilo":
    score = score + 0.5
elif answer == "Tiburón":
    score = score + 1.0

# Ejercicio 5
score = 0
points = 0
answer1 = input("¿Pregunta? \n1\n2\n3\n4")

if answer1 == 1:
    points = points + 4
elif answer1 == 2:
    points = points + 3
elif answer1 == 3:
    points = points + 2
elif answer1 == 4:
    points = points + 1

answer2 = input("¿Pregunta? \n1\n2\n3\n4")

if answer2 == 1:
    points = points + 4
elif answer2 == 2:
    points = points + 3
elif answer2 == 3:
    points = points + 2
elif answer2 == 4:
    points = points + 1

answer3 = input("¿Pregunta? \n1\n2\n3\n4")

if answer3 == 1:
    points = points + 4
elif answer3 == 2:
    points = points + 3
elif answer3 == 3:
    points = points + 2
elif answer3 == 4:
    points = points + 1

if points < 7.2:
    score = 3.0 * (points / 7.2) + 1.0
else:
    score = 3.0 * ((points -7.2) / 4.8) + 4.0

print(f"Su puntaje fue de {points} y su nota es {score}")