#! Python3
# Get score based on user input

answer = input(
    "¿Cuál de los siguientes animales vive en el agua? \nPerro\nCocodrilo\nConejo\nTiburón"
)
score = 0

if answer == "Cocodrilo":
    score = score + 0.5
elif answer == "Tiburón":
    score = score + 1.0
