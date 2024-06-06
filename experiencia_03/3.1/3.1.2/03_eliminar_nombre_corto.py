#! Python3
# Ask to user for names, then delete the shortest one

# initialize variables
names = []

# adding names
add_names = True
while add_names == True:
    name = input("Ingrese un nombre\n> ")
    names.append(name)
    while True:
        choice = input("Desea agregar otro nombre? (si/no)\n> ").lower()
        if choice == "si":
            break
        elif choice == "no":
            add_names = False
            break
        else:
            print("Opción inválida (si/no)")


# get shortest name length, iterate to find the first ocurrence where the length of the string equals to the shortest length,
# save it in a variable
min_length = min(len(name) for name in names)
shortest_name = ""

for i, item in enumerate(names):
    if len(item) == min_length:
        shortest_name = item

# remove the name, print list
names.remove(shortest_name)
print(names)
