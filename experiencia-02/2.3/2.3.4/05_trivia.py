#! Python3
# Get points and score based on a series of questions

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
    score = 3.0 * ((points - 7.2) / 4.8) + 4.0

print(f"Su puntaje fue de {points} y su nota es {score}")
