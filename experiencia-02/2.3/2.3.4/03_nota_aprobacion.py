#! Python3
# Ask for partial grades, calculate if student pass or not

# ask for grades
nota1 = int(input("Ingrese la primera nota"))
nota2 = int(input("Ingrese la segunda nota"))
nota3 = int(input("Ingrese la tercera nota"))

# calculate average
promedio = (nota1 + nota2 + nota3) / 3

# prints whether the average grade is a passing grade or a failing grade
if promedio > 4.0:
    print("Aprobado")
else:
    print("Reprobado")
