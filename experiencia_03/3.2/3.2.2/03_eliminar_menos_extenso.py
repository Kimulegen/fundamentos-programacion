#! Python3
# Ask for names, remove the shortest one

# importing os for clear
import os

# initialize variables
names = []

# ask for names, adding them to a list
add_names = True
while add_names == True:
    os.system("cls||clear")
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

# sort list by string length, remove first item in the sorted list
names.sort(key=len)
shortest_name = names.pop(0)

# show names list
print(f"el nombre eliminado fue '{shortest_name}'")
