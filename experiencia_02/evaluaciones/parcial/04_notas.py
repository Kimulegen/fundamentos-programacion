nota = int(input("Ingrese una nota\n> "))
calificacion = ""

if 65 <= nota <= 70:
    calificacion = "A"
elif 50 <= nota <= 64:
    calificacion = "B"
elif 40 <= nota <= 49:
    calificacion = "C"
elif 30 <= nota <= 39:
    calificacion = "D"
else:
    calificacion = "F"

print(f"Su calificación es: {calificacion}")