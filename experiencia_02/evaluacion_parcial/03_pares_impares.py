odd_counter = 0
even_counter = 0

num = int(input("Ingrese un numero entero positivo\n> "))

for i in range(1,num+1):
    if i % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1

print(f"la cantidad de números pares en el rango es de {even_counter}")
print(f"la cantidad de números impares en el rango es de {odd_counter}")