#! Python3
# Store names and ages in a list, create a set with the ages of said list

# initialize variables
data = []
age_set = set()

# ask for names and their ages, store them in a list
while True:
    name = input("Ingrese un nombre: ")
    if name.lower() == "fin":
        break
    age = int(input("Ingrese la edad: "))
    data.append((name, age))

# Store the ages in a set
for item in data:
    age_set.add(item[1])


# ALTERNATIVE ANSWER
edades_unicas = {edad for _, edad in data}
print(edades_unicas)
