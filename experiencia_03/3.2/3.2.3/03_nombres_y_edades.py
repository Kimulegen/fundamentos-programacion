data = []

while True:
    name = input("Ingrese un nombre: ")
    if name.lower() == "fin":
        break
    age = int(input("Ingrese la edad: "))
    data.append((name,age))

age_set = set()
for item in data:
    age_set.add(item[1])

# ALGO EJERCICIO
edades_unicas = {edad for _, edad in data}
print(edades_unicas)