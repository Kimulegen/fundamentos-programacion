#! Python
# Calculate the total payment for cargo transportation based on weight categories and quantity,
# using a for loop

# initialize variables
n_bultos = int(input("Ingrese la cantidad de bultos"))
livianos = 0
normales = 0
total_liviano = 0
total_normal = 0

# calculate payment based on weight
for i in n_bultos:
    peso = int(input(f"Ingresa el peso del bulto {i} (en kg)"))

    if 1 <= peso <= 5:
        livianos += 1
        total_liviano += 1000
    elif 6 <= peso <= 10:
        normales += 1
        total_normal += 2000
    else:
        print("Bulto demasiado pesado, favor ingrese otro")

# show cargo info
print(f"{livianos} bulto(s) liviano(s) ${total_liviano}")
print(f"{normales} bulto(s) normal(es) ${total_normal}")
print(f"Valor total a pagar: ${total_liviano + total_normal}")
